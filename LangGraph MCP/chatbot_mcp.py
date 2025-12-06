from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import requests
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()


llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash') 


# Create the tools


client = MultiServerMCPClient(
    {
        "DEMO Server": {
        "transport":"stdio",
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "E:\\Machine Learning and Data Science\\Model-Contex-Protocol\\Calculator MCP Server\\main.py"
            ]
        },
        "expense":{
        "transport":"streamable_http",
        "url": "https://thoughtless-silver-snake.fastmcp.app/mcp"
        }
    }
)



#################################################################################


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


async def build_graph():

    tools = await client.get_tools()

    print(tools)

    llm_with_tools = llm.bind_tools(tools)


    async def chat_node(state: ChatState):
        messages = state['messages']
        response = await llm_with_tools.ainvoke(messages)
        return {"messages": [response]}

    tool_node = ToolNode(tools)

    ######################################

    # Graph 
    # graph Structure

    graph = StateGraph(ChatState)
    graph.add_node('chat_node',chat_node)
    graph.add_node('tools',tool_node)


    graph.add_edge(START,'chat_node')

    graph.add_conditional_edges("chat_node",tools_condition)

    graph.add_edge('tools','chat_node')

    chatbot = graph.compile()

    return chatbot

async def main():

    chatbot = await build_graph()

    result = await chatbot.ainvoke({"messages": [HumanMessage(content="add the expenses of 200 for transport cab?")]})


    print(result['messages'][-1].content)


if __name__ == "__main__":
    asyncio.run(main())