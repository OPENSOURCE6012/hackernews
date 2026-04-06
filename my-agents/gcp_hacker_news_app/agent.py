import os
import sys
from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox_url = os.environ.get("TOOLBOX_URL")  # ← FIXED

if not toolbox_url:
    raise RuntimeError("TOOLBOX_URL is required but not set.")

tools = []
try:
    print(f"Connecting to Toolbox at: {toolbox_url}")
    toolbox = ToolboxSyncClient(toolbox_url)
    try:
        tools = toolbox.load_toolset("hackernews_tools")
        print(f"Loaded toolset 'hackernews_tools': {len(tools)} tool(s).")
    except Exception as e1:
        print(f"Toolset not found: {e1}. Trying individual tools...")
        try:
            tools = [
                toolbox.load_tool("list_stories"),
                toolbox.load_tool("query_comments"),
            ]
            print(f"Loaded individual tools: {len(tools)} tool(s).")
        except Exception as e2:
            print(f"ERROR: Could not load individual tools: {e2}", file=sys.stderr)
            raise RuntimeError(f"Failed to load tools: {e2}")
except RuntimeError:
    raise
except Exception as e:
    print(f"ERROR: Toolbox connection failed: {e}", file=sys.stderr)
    raise RuntimeError(f"Could not connect to Toolbox: {e}")

root_agent = Agent(
    name="hacker_news_agent",
    model="gemini-2.5-flash",
    description="Query Hacker News dataset.",
    instruction="""
You are a Hacker News assistant. Be proactive — never ask for confirmation, just call the tool immediately.

You have access to ONLY these tools:
- list_stories: Retrieves top 10 Hacker News stories. NO parameters needed.
- query_comments: Gets comments for a story. Requires parent_id (integer).

Rules:
- When user says hi/hello → greet them briefly and immediately call list_stories()
- When asked for stories/news/data → call list_stories() immediately, no questions asked
- When asked for comments → ask for story ID if not provided, then call query_comments
- NEVER invent new tool names or parameters
- NEVER say "Would you like me to..." — just do it
""",
    tools=tools,
)