# LangGraph

Comprehensive guide and reference for the LangGraph collection of example workflows and notebooks.

LangGraph is a hands-on collection demonstrating how to design modular, stateful, and multi-agent LLM applications using graph-based workflows. This repository groups real example notebooks across different workflow patterns — sequential, conditional, iterative, parallel — and includes examples for persistence, tools, and practical chatbot setups.

---

## Table of Contents

- **Project Overview**: What this repo contains and goals
- **Repository Structure**: Descriptions of folders and files
- **Setup**: Python, virtual environment, and dependencies
- **Running Notebooks**: How to open and run examples
- **Workflow Summaries**: What each notebook demonstrates
- **Troubleshooting**: Common issues and fixes
- **Contributing**: How to contribute
- **Contact & License**

---

## Project Overview

This repository is a curated set of Jupyter notebooks that illustrate practical LangGraph workflows and patterns for building LLM-driven applications. Each notebook is self-contained and demonstrates one or more patterns such as:

- Chatbot flows with memory and state
- Conditional branching and decision trees
- Iterative generation and refinement loops
- Parallel workflows for concurrent tasks
- Persistence strategies for storing state and results
- Tool integration and helper utilities

The examples are suitable for learning, prototyping, and adapting to production workflows.

---

## Repository Structure

Top-level files:

- `README.md`: This file — full project overview and usage.
- `requirements.txt`: Python dependency list for running the notebooks.

Top-level directories (each contains one or more Jupyter notebooks):

- `LangGraph ChatBot WorkFlow/` — `chatbot.ipynb` : Chatbot example demonstrating conversation flow, memory, and prompt handling.
- `LangGraph conditional WorkFlow/` — `quadratic_workflow.ipynb`, `review_reply_workflow.ipynb` : Examples of conditional branching and decision logic inside LangGraph workflows.
- `LangGraph Iterative WorkFlow/` — `post_generator_twitter.ipynb` : Iterative prompt/refinement pattern for generating social media posts.
- `LangGraph Parallel WorkFlow/` — `batsman_workflow.ipynb`, `Upsc_essay_workflow.ipynb` : Parallel task execution patterns and aggregation of results.
- `LangGraph Persitence/` — `persitence.ipynb` : Persistence patterns (note: folder name is spelled `Persitence` in this repo) showing state saving and retrieval strategies.
- `LangGraph Sequential WorkFlows/` — `BMI_WorkFlow.ipynb`, `Prompt_chaining_workflow.ipynb`, `Simple_LLM_Workflow.ipynb`, `test_installation.ipynb` : Sequential pipelines and prompt chaining examples, plus an environment test notebook.
- `LangGraph Tools/` — `tools.ipynb` : Utility examples, integrations, and tooling for building and debugging LangGraph flows.

> Note: Filenames and folder names are case-sensitive on some platforms; use the exact names shown above when opening files.

---

## Setup

Recommended Python environment:

- Python 3.10 or 3.11

Quick setup (PowerShell):

```powershell
# create and activate a virtual environment (PowerShell)
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# upgrade pip and install dependencies
python -m pip install --upgrade pip; pip install -r requirements.txt
```

If some notebooks require extra packages not present in `requirements.txt`, install them individually. For example, during development the following packages were used and may be helpful:

```powershell
pip install langchain_community ddgs
```

---

## Running Notebooks

Open the repository in VS Code or launch Jupyter Notebook / Jupyter Lab from the repo root:

```powershell
# start Jupyter Lab (recommended)
jupyter lab

# or classic notebook UI
jupyter notebook
```

Then open any of the notebooks inside the folders listed under **Repository Structure**.

Tips:

- Use the `test_installation.ipynb` in `LangGraph Sequential WorkFlows/` to verify kernel and dependencies.
- If you hit import errors, ensure your virtual environment is activated and the kernel in Jupyter matches `.venv`'s Python interpreter.

---

## Workflow Summaries (what each notebook demonstrates)

- `LangGraph ChatBot WorkFlow/chatbot.ipynb`:

  - Demonstrates building a stateful conversational agent, handling user messages, and persisting short-term memory during a session.

- `LangGraph conditional WorkFlow/quadratic_workflow.ipynb`:

  - An example of branching logic based on inputs and intermediate results (e.g., choose different processing paths depending on data).

- `LangGraph conditional WorkFlow/review_reply_workflow.ipynb`:

  - Shows conditional reply generation for reviews and decision rules that change the prompt path.

- `LangGraph Iterative WorkFlow/post_generator_twitter.ipynb`:

  - Iterative prompt refinement: generate drafts, evaluate, and refine until quality threshold is met.

- `LangGraph Parallel WorkFlow/batsman_workflow.ipynb` and `Upsc_essay_workflow.ipynb`:

  - Parallelize sub-tasks (e.g., multiple prompt calls or summarization tasks) and then aggregate results.

- `LangGraph Persitence/persitence.ipynb`:

  - Patterns for saving workflow outputs and agent state to disk or external stores (note: folder name spelled `Persitence`).

- `LangGraph Sequential WorkFlows/*`:

  - `BMI_WorkFlow.ipynb`: simple sequential pipeline to compute BMI and provide recommendations.
  - `Prompt_chaining_workflow.ipynb`: prompt chaining examples to build complex behaviors from small prompt steps.
  - `Simple_LLM_Workflow.ipynb`: minimal end-to-end example to show the skeleton of a LangGraph workflow.
  - `test_installation.ipynb`: environment and dependency checks.

- `LangGraph Tools/tools.ipynb`:
  - Helper utilities, debugging patterns, and small tools that support the workflows (e.g., prompt templates, validators).

Each notebook usually contains:

- Problem statement and expected input/output
- Setup cell to install/import required libs
- Step-by-step LangGraph node construction or pseudo-code
- Example runs and inspection of results

---

## Troubleshooting

- Kernel mismatch / imports not found: ensure the Jupyter kernel points to the activated `.venv` interpreter.
- Long-running prompts or rate limits: add retries and backoff in notebook cells when calling external LLM APIs.
- Path or filename errors on Windows: watch for spaces in folder names and escape paths or use quotes when running commands.

If you need help reproducing an error, open an issue with the notebook name, the error traceback, and your Python version.

---

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repo and create a branch for your changes.
2. Add or update a notebook demonstrating a new pattern or fix.
3. Update `requirements.txt` if you add new dependencies.
4. Open a pull request with a clear description and mention which notebook(s) you changed.

Guidelines:

- Keep notebooks focused and reproducible: include necessary install/import cells and short README notes inside the notebook.
- Avoid committing large binary outputs; clear large outputs before committing.

---

## Contact

If you have questions or want to collaborate, open an issue or reach out to the repository owner.

---

## License

Specify your license here if you have one (e.g., MIT, Apache-2.0) — add a `LICENSE` file at the repo root if desired.

---

## Quick Start Checklist

- [ ] Create and activate a Python virtual environment
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Launch `jupyter lab` and run `test_installation.ipynb`
- [ ] Open the workflow notebook of interest and run the cells sequentially

Enjoy exploring LangGraph workflows! If you'd like, I can also:

- Add short READMEs inside each folder summarizing the notebook(s)
- Create a small runnable example script that executes one of the notebooks programmatically
