# LangGraph Learning Repository

A project-focused, education-first collection of LangGraph workflows for learning by pattern.

This repository is organized as a set of practical notebooks and scripts that demonstrate how to design LLM applications using graph-based control flow:

- Sequential workflows
- Conditional routing
- Iterative refinement loops
- Parallel branches with merge
- Persistence and time-travel style replay
- Human-in-the-loop interrupts
- Tool-calling agents
- RAG with vector retrieval
- Subgraphs and state sharing
- MCP (Model Context Protocol) integration
- Basic LLM memory behavior comparisons

Use this README as your revision sheet.

## 1. Repository Overview

Root contents:

- `README.md`: This guide.
- `requirements.txt`: Currently empty, so dependencies must be installed manually.
- `.env`: Local secrets (API keys). Not committed in normal workflows.
- `islr.pdf`: Document used by the RAG notebook.
- `venv/`: Local virtual environment folder.

Main learning folders:

- `LangGraph Sequential WorkFlows/`
- `LangGraph conditional WorkFlow/`
- `LangGraph Iterative WorkFlow/`
- `LangGraph Parallel WorkFlow/`
- `LangGraph Persitence/`
- `LangGraph ChatBot WorkFlow/`
- `LangGraph Human In The Loop (HITL)/`
- `LangGraph Tools/`
- `LangGraph RAGS/`
- `LangGraph SubGraph/`
- `LangGraph MCP/`
- `LLM Memory/`

## 2. Skills You Build In This Repo

By completing the notebooks in order, you practice:

1. Defining graph state with `TypedDict`.
2. Writing node functions that transform state.
3. Connecting nodes with `add_edge` for deterministic flows.
4. Branching with `add_conditional_edges` for decision-based routing.
5. Creating loops for iterative improvement.
6. Running independent branches in parallel and merging outputs.
7. Using checkpointing (`MemorySaver` / in-memory checkpointer).
8. Building tool-enabled agents using `ToolNode` + `tools_condition`.
9. Inserting human approval steps with `interrupt` + `Command(resume=...)`.
10. Building modular systems using subgraphs.
11. Adding retrieval pipelines (RAG) with vector stores.
12. Connecting external capability servers through MCP.

## 3. Detailed Folder and File Guide

### 3.1 `LangGraph Sequential WorkFlows/`

Purpose: Understand the most basic graph pattern (linear pipelines).

Files:

- `LangGraph Sequential WorkFlows/test_installation.ipynb`
  - Minimal import check (`StateGraph`) to confirm setup.

- `LangGraph Sequential WorkFlows/Simple_LLM_Workflow.ipynb`
  - State: question -> answer.
  - Node: `llm_qa`.
  - Graph shape: `START -> llm_qa -> END`.
  - Concept: Smallest functional LangGraph + LLM example.

- `LangGraph Sequential WorkFlows/Prompt_chaining_workflow.ipynb`
  - Nodes: `create_outline`, `create_blog`.
  - Graph shape: `START -> create_outline -> create_blog -> END`.
  - Concept: Prompt chaining where output of one step feeds next step.

- `LangGraph Sequential WorkFlows/BMI_WorkFlow.ipynb`
  - Nodes: `calculate_bmi`, `label_bmi`.
  - Graph shape: `START -> calculate_bmi -> label_bmi -> END`.
  - Concept: Pure deterministic workflow without LLM dependency.

### 3.2 `LangGraph conditional WorkFlow/`

Purpose: Learn branching decisions using conditional edges.

Files:

- `LangGraph conditional WorkFlow/quadratic_workflow.ipynb`
  - Nodes: `show_equation`, `calculate_discriminant`, `real_roots`, `repeated_roots`, `no_real_roots`.
  - Conditional router: `check_condition`.
  - Concept: Traditional algorithmic branching through graph routing.

- `LangGraph conditional WorkFlow/review_reply_workflow.ipynb`
  - Nodes: `find_sentiment`, `positive_response`, `run_diagnosis`, `negative_response`.
  - Conditional router: `check_sentiment`.
  - Uses structured outputs with Pydantic schemas.
  - Concept: LLM-based classification followed by route-specific response logic.

### 3.3 `LangGraph Iterative WorkFlow/`

Purpose: Build evaluation-improvement loops.

Files:

- `LangGraph Iterative WorkFlow/post_generator_twitter.ipynb`
  - Nodes: `generate_tweet`, `evaluate_tweet`, `optimize_tweet`.
  - Conditional loop router: `route_evaluation`.
  - Loop behavior: keeps optimizing until evaluation becomes `approved`.
  - Concept: Self-refining generation workflow.

### 3.4 `LangGraph Parallel WorkFlow/`

Purpose: Run independent analysis branches concurrently and aggregate.

Files:

- `LangGraph Parallel WorkFlow/batsman_workflow.ipynb`
  - Parallel nodes: `calculate_sr`, `calculate_bpb`, `calculate_boundary_percent`.
  - Merge node: `summary`.
  - Concept: Multi-metric computation in parallel.

- `LangGraph Parallel WorkFlow/Upsc_essay_workflow.ipynb`
  - Parallel evaluators: language, analysis, thought.
  - Merge node: `final_evaluation`.
  - Uses structured outputs via Pydantic.
  - Concept: Multi-dimensional grading pipeline.

### 3.5 `LangGraph ChatBot WorkFlow/`

Purpose: Stateful chatbot baseline with memory/checkpointing.

Files:

- `LangGraph ChatBot WorkFlow/chatbot.ipynb`
  - State: message history with `add_messages`.
  - Node: `chat_node`.
  - Checkpointer: `MemorySaver`.
  - Concept: conversational state graph with thread-based continuity.

### 3.6 `LangGraph Persitence/` (folder name intentionally as in repo)

Purpose: Persist workflow state and revisit conversation progress.

Files:

- `LangGraph Persitence/persitence.ipynb`
  - Nodes: `generate_joke`, `generate_explanation`.
  - Checkpointer enabled at compile-time.
  - Concept: workflow persistence and replay-style behavior.

### 3.7 `LangGraph Human In The Loop (HITL)/`

Purpose: Add explicit human approval in graph execution.

Files:

- `LangGraph Human In The Loop (HITL)/01_hitl.ipynb`
  - Uses `interrupt` and `Command(resume=...)`.
  - Concept: pausing workflow for human decision before continuing.

- `LangGraph Human In The Loop (HITL)/chatbot_without_hitl.py`
  - Tool-enabled stock assistant.
  - Tools: `get_stock_price`, `purchase_stock` (mock auto-success).
  - Graph: `chat_node <-> tools` loop using `tools_condition`.

- `LangGraph Human In The Loop (HITL)/chatbot_with_hitl.py`
  - Same stock assistant but `purchase_stock` triggers `interrupt` for approval.
  - Concept: practical comparison between autonomous and approval-gated flows.

### 3.8 `LangGraph Tools/`

Purpose: Tool-calling agent design with external APIs.

Files:

- `LangGraph Tools/tools.ipynb`
  - Tools include calculator + stock API + DuckDuckGo search.
  - Uses `ToolNode`, `@tool`, and `tools_condition` routing.
  - Concept: LLM decides when to call tools and returns synthesized final answer.

### 3.9 `LangGraph RAGS/`

Purpose: Retrieval-Augmented Generation with LangGraph tool routing.

Files:

- `LangGraph RAGS/langGraph_rag.ipynb`
  - Loads PDF via `PyPDFLoader`.
  - Splits text with `RecursiveCharacterTextSplitter`.
  - Builds FAISS vector store + retriever.
  - Exposes retrieval as a tool in graph (`ToolNode`).
  - Concept: agentic RAG where graph decides retrieval usage.

### 3.10 `LangGraph SubGraph/`

Purpose: Modular graph design and parent-child workflow composition.

Files:

- `LangGraph SubGraph/basic_approch.ipynb`
  - Basic two-step answer -> translation flow.

- `LangGraph SubGraph/subgraph.ipynb`
  - Explicit subgraph creation with parent graph integration.

- `LangGraph SubGraph/subgraph_sharestate.ipynb`
  - Subgraph with shared state handling.

Core concept in all three:

- Build reusable sub-pipelines and compose them into larger systems.

### 3.11 `LangGraph MCP/`

Purpose: Connect LangGraph agents to MCP servers.

Files:

- `LangGraph MCP/chatbot_async.py`
  - Async tool-enabled graph with local tools.
  - Tools: calculator, stock fetch, DuckDuckGo search.
  - Uses Gemini model and async invocation.

- `LangGraph MCP/chatbot_mcp.py`
  - Uses `MultiServerMCPClient`.
  - Connects to:
    - local stdio MCP server (`uv run ... fastmcp ...`)
    - remote streamable HTTP MCP server.
  - Dynamically loads MCP tools and binds them to LLM.
  - Concept: external capability extension through MCP protocol.

### 3.12 `LLM Memory/`

Purpose: Demonstrate short-term memory behavior difference.

Files:

- `LLM Memory/example1_no_STM.ipynb`
  - Direct separate prompts with no explicit conversation list.
  - Concept: memory loss across isolated calls.

- `LLM Memory/example2_STM.ipynb`
  - Manual message list maintained across turns.
  - Concept: preserving context by carrying conversation history.

## 4. Common Graph Architecture Used Across Repo

Most agentic notebooks/scripts follow this recurring architecture:

1. Define `State` (`TypedDict`, sometimes with `Annotated` reducers).
2. Initialize LLM(s) and optional tools.
3. Build nodes (plain Python functions).
4. Register nodes with `StateGraph(...)`.
5. Add deterministic and/or conditional edges.
6. Compile graph (optionally with checkpointer).
7. Invoke graph with initial state.

Typical tool-agent pattern:

- `START -> chat_node`
- conditional routing from `chat_node` via `tools_condition`
- `tools -> chat_node` loop
- terminate when model emits non-tool response

## 5. Setup and Installation

### 5.1 Python version

Recommended:

- Python 3.10 or 3.11

### 5.2 Virtual environment (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### 5.3 Install dependencies

`requirements.txt` is currently empty, so install manually:

```powershell
pip install langgraph langchain langchain-core langchain-community langchain-google-genai langchain-huggingface langchain-mcp-adapters langchain-text-splitters faiss-cpu pydantic python-dotenv requests jupyter
```

If you run MCP examples:

```powershell
pip install uv fastmcp
```

## 6. Environment Variables

Create/update `.env` with the keys your notebooks/scripts use.

Likely required (based on imports/models):

- `GOOGLE_API_KEY` for Gemini (`ChatGoogleGenerativeAI`)
- `HUGGINGFACEHUB_API_TOKEN` for `HuggingFaceEndpoint`
- Optional provider keys depending on experiments

Notes:

- Some files include Alpha Vantage API key directly in source; move this to env variables for safety.
- Never commit real secrets.

## 7. How To Run

### 7.1 Run notebooks

```powershell
jupyter lab
```

Then execute notebooks in this recommended order:

1. `LangGraph Sequential WorkFlows/test_installation.ipynb`
2. `LangGraph Sequential WorkFlows/Simple_LLM_Workflow.ipynb`
3. `LangGraph Sequential WorkFlows/Prompt_chaining_workflow.ipynb`
4. `LangGraph conditional WorkFlow/quadratic_workflow.ipynb`
5. `LangGraph conditional WorkFlow/review_reply_workflow.ipynb`
6. `LangGraph Iterative WorkFlow/post_generator_twitter.ipynb`
7. `LangGraph Parallel WorkFlow/batsman_workflow.ipynb`
8. `LangGraph Parallel WorkFlow/Upsc_essay_workflow.ipynb`
9. `LangGraph Persitence/persitence.ipynb`
10. `LangGraph ChatBot WorkFlow/chatbot.ipynb`
11. `LangGraph Tools/tools.ipynb`
12. `LangGraph RAGS/langGraph_rag.ipynb`
13. `LangGraph Human In The Loop (HITL)/01_hitl.ipynb`
14. `LangGraph SubGraph/basic_approch.ipynb`
15. `LangGraph SubGraph/subgraph.ipynb`
16. `LangGraph SubGraph/subgraph_sharestate.ipynb`
17. `LLM Memory/example1_no_STM.ipynb`
18. `LLM Memory/example2_STM.ipynb`

### 7.2 Run Python scripts

```powershell
python "LangGraph Human In The Loop (HITL)\chatbot_without_hitl.py"
python "LangGraph Human In The Loop (HITL)\chatbot_with_hitl.py"
python "LangGraph MCP\chatbot_async.py"
python "LangGraph MCP\chatbot_mcp.py"
```

## 8. Revision Notes (Exam-Style)

Use this checklist while revising:

- Can I explain state design and reducers (`add_messages`)?
- Can I draw graph topology for each pattern type?
- Can I implement conditional routing from scratch?
- Can I build an iterative loop with exit conditions?
- Can I combine parallel branches and aggregate safely?
- Can I add checkpointing and thread-based continuation?
- Can I insert human approval with `interrupt`/`resume`?
- Can I convert a retriever into a callable tool for agentic RAG?
- Can I separate logic into subgraphs and compose parent flow?
- Can I reason about tool safety (network calls, API keys, errors)?

## 9. Known Gaps and Improvements

Current repository gaps:

- `requirements.txt` is empty.
- Folder/file spelling variants (`Persitence`, `approch`) may confuse automation.
- API key for Alpha Vantage appears hardcoded in scripts.
- Some notebooks have no markdown explanation cells.

Recommended improvements:

1. Populate `requirements.txt` with pinned versions.
2. Add short markdown intro/output expectations to each notebook.
3. Move all secret keys to `.env` only.
4. Add one small `tests/` folder for deterministic graph examples.
5. Add architecture diagrams (Mermaid) per workflow category.

## 10. Quick Start (Short Version)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install langgraph langchain langchain-core langchain-community langchain-google-genai langchain-huggingface langchain-mcp-adapters langchain-text-splitters faiss-cpu pydantic python-dotenv requests jupyter
jupyter lab
```

Then start with:

- `LangGraph Sequential WorkFlows/test_installation.ipynb`
- `LangGraph Sequential WorkFlows/Simple_LLM_Workflow.ipynb`

That gives you the base needed for all advanced folders.
