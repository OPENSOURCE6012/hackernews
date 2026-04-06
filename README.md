HackerNews Intelligence Agent (Vertex AI Edition) 📡🤖

HackerNews Intelligence Agent is a sophisticated analysis tool that monitors Hacker News for tech trends. This version is powered by Google Cloud Vertex AI, providing enterprise-grade security and access to the latest Gemini models without the need for static API keys.
🚀 Key Features

    Native Google Cloud Integration: Uses IAM roles instead of vulnerable API keys.

    Gemini-Powered Analysis: Leverages Vertex AI for high-fidelity summarization of HN threads.

    Trend Detection: Automatically extracts keywords and developer sentiment from top stories.

    MCP Architecture: Built on the Model Context Protocol for seamless tool-to-agent communication.

📂 Project Structure
Plaintext

.
├── mcp-toolbox/    # MCP tools for Hacker News API interaction
├── my-agents/      # Agent logic (Vertex AI / Gemini integration)
├── .gitignore      # Standard excludes (now includes .env for Project IDs)
└── README.md       # Project documentation

🛠️ Google Cloud Setup

Before running the agent, you must prepare your Google Cloud environment:

    Enable the Vertex AI API:
    Bash

    gcloud services enable aiplatform.googleapis.com

    Set your Project ID:
    Find your Project ID in the Cloud Console and set it in your environment:
    Bash

    export GOOGLE_CLOUD_PROJECT="your-project-id"
    export GOOGLE_CLOUD_LOCATION="us-central1"

    Authentication:
    Since you are in Cloud Shell, you are already authenticated. If you move to a local machine later, run:
    Bash

    gcloud auth application-default login

⚙️ Configuration

Create a .env file to store your project details:
Plaintext

PROJECT_ID=endless-empire-472415-f4
LOCATION=us-central1
MODEL_NAME=gemini-1.5-pro

🤖 Usage

Run the agent to fetch and analyze the top 5 stories currently trending on Hacker News:
Bash

python3 my-agents/hn_agent.py --limit 5

⚠️ Large File Warning

The toolbox binary in mcp-toolbox/ is excluded from this repo via .gitignore as it exceeds GitHub's 100MB limit. Ensure you build it locally before execution.
📜 License

MIT License - See LICENSE for details.
Pro-Tip for your Code:

When you write your Python code for this agent, make sure you initialize the Vertex AI SDK like this:
Python

import vertexai
from vertexai.generative_models import GenerativeModel
import os

# No API key needed!
vertexai.init(project=os.getenv("PROJECT_ID"), location=os.getenv("LOCATION"))
model = GenerativeModel("gemini-1.5-pro")
