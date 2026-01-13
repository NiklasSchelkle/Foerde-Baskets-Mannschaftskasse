🤖 Smol-Quant: Autonomous Financial Analyst Agent
📖 Project Overview

Smol-Quant is an autonomous agentic system designed to simulate the workflow of a junior financial analyst. Developed as a capstone project for the "Generative AI" course, this system addresses the fundamental limitations of standard LLMs in financial contexts.
The Problem

Standard LLMs frequently hallucinate financial data when asked to perform precise calculations or retrieve up-to-date market information. They lack access to verified internal datasets and often fail to distinguish between creative writing and factual reporting.
The Solution: Grounded Truth

The agent cannot invent numbers. It must retrieve them from two distinct, verified data sources:

    Structured Data: A comprehensive NASDAQ-100 dataset (CSV) for hard metrics like PE Ratio, Volatility, and Market Cap.

    Unstructured Data: A Vector Database (ChromaDB) containing news, business summaries, and context from sources like Wikipedia and Yahoo Finance.

🏗️ System Architecture
1. The Brain: CodeAgent (Orchestrator)

At the core lies the CodeAgent. Unlike a simple chatbot, this component acts as a reasoning engine. It writes and executes Python code to solve complex problems.
2. The Logic: ReAct Pattern

The agent follows the ReAct (Reasoning + Acting) paradigm. For every user query, it autonomously cycles through:

    Reasoning: Analyzing the user's intent.

    Tool Selection: Deciding which specific tool is required.

    Observation: Reading the output of the tool execution to inform the next step.

3. The Safety: LLM-as-a-Judge Pipeline

To ensure operational safety, we implemented a "Compliance Officer" layer. This secondary model intercepts every draft response before it reaches the user.

    Compliance Check: Scans for financial advice violations or hallucinations.

    Self-Correction Loop: If the Judge rejects an answer, the feedback is injected back into the agent's memory, forcing it to replan and correct its output automatically.

🛠️ The Toolset

The agent is sandboxed and equipped with three specialized tools to handle different data modalities.
1. EDA Tool (eda_summary)

    Function: Acts as the data scout.

    Capability: Provides the agent with metadata, column structures, and statistical summaries of the NASDAQ-100 dataset. This allows the agent to understand the "shape" of the data before performing deep analysis.

2. Financial Analyst Tool (financial_analyst)

    Function: The RAG (Retrieval Augmented Generation) interface.

    Capability: Performs semantic searches within the ChromaDB vector store. It retrieves qualitative context—such as recent strategic challenges or leadership changes—to explain the "why" behind the numbers.

3. Image Generation Tool (image_generation_tool)

    Function: The visual artist.

    Capability: Connects to generative image models (DALL-E 3) to create illustrative visuals for abstract concepts, such as "market sentiment" or "bull runs," adding a multi-modal dimension to the report.

🔒 Security & Sandbox Environment

To prevent the agent from executing malicious code, the CodeAgent operates within a restricted local sandbox. It does not have unrestricted access to the host machine's shell or file system.
Allowed Libraries

The agent is strictly limited to importing only a specific set of safe libraries required for data analysis and visualization. Any attempt to import unauthorized modules (e.g., os, sys, requests) is blocked by the runtime.

Authorized Imports:

    pandas (Data Manipulation)

    numpy (Numerical Computing)

    matplotlib.pyplot & seaborn (Data Visualization)

    io, base64, json, ast (Data Processing)

📂 Project Structure
Plaintext

GenAI/
├── agent/
│   ├── agent_builder.py       # Factory: Assembles the Agent, Persona, and Safety Prompts
│   └── tools/                 # Tool Definitions
├── data/
│   ├── chroma_db/             # Persistent Vector Store (Embeddings)
│   └── nasdaq_100...csv       # Structured Financial Dataset
├── data_ingestions/
│   └── data_scraping_embedding.py # Scrape, structure, and embed data
├── evaluate_agent.py          # Offline Evaluation Pipeline
├── main.py                    # CLI Entry Point
├── app.py                     # Streamlit Web Interface
└── docker-compose.yml         # Container Orchestration

⚙️ Installation & Setup
Prerequisites

    OpenAI API Key

    Docker & Docker Compose (Recommended) OR Python 3.10+

1. Configuration

Create a .env file in the root directory:
Ini, TOML

OPENAI_API_KEY=sk-proj-xxxxxx...

🐳 Docker: Easy Start (Recommended)

To avoid dependency conflicts and ensure a consistent environment, Smol-Quant is fully containerized. This method bypasses the need for manual Python environment setup.
1. Build and Start the Container
Bash

docker-compose up --build -d

2. Initialize Data (Scraping & Embedding)

The database is empty on the first start. Trigger the ingestion script inside the container:
Bash

docker exec -it smol_quant_app python data_ingestion/data_scraping_embedding.py

Note: This script automatically cleans up legacy database entries to ensure a fresh "Source of Truth".
3. Access the Web UI

Open your browser at: 👉 http://localhost:8501
🛠️ Manual Installation (Alternative)
1. Environment Setup
Bash

# Windows
python -m venv genai
genai\Scripts\activate

# macOS / Linux
python3 -m venv genai
source genai/bin/activate

2. Install Dependencies
Bash

pip install -r requirements.txt

🚀 Usage
1. Web Interface (Streamlit)
Bash

streamlit run app.py

2. Evaluation Pipeline
Bash

python evaluate_agent.py

📊 Methodology & Evaluation

To ensure academic rigor, we implemented an automated evaluation framework inspired by Google's Purpose-Driven Evaluation. We test against a Golden Dataset covering diverse scenarios.

    Pillar 1: Agent Success & Quality: Verified by comparing agent-extracted numbers against ground truth using a semantic LLM Judge.

    Pillar 2: Process & Trajectory: Verified by a heuristic validator that ensures the agent selects the correct tool.

    Pillar 3: Trust & Safety: Verified by "Negative Tests" to ensure the agent reports "Data Missing" rather than hallucinating metrics.

✨ Features & Capabilities
✅ Core Components (Course Requirements)

    Retrieval Augmented Generation (RAG): Queries ChromaDB for news and summaries.

    Data Analysis & Code Execution: Executes pandas code for structured data analysis.

    Multi-step Agent Pipeline: Planner-Executor model with an LLM Compliance Officer.

    Image Generation Integration: DALL-E 3 integration for conceptual visuals.

🌟 Bonus & Advanced Features

    Scientific Evaluation Pipeline: Custom audit framework for performance metrics.

    Chain-of-Thought Visualization: Transparent reasoning traces in the UI.

    Conversation Memory: Persistent session state for multi-turn dialogue.

    Self-Correction Loop: Automated feedback loop for compliance failures.

Möchtest du, dass ich noch ein automatisches Inhaltsverzeichnis mit Sprungmarken (Anchors) ganz oben hinzufüge, damit die README noch übersichtlicher wird?
