from langchain.tools import Tool
from dotenv import load_dotenv
import requests
import os

load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")

def web_search(query):
    res = requests.post(
        "https://api.tavily.com/search",
        headers={"Authorization": f"Bearer {tavily_api_key}"},
        json={"query": query}, 
        timeout=10
    )
    return res.json()["results"][0]["content"]


WebSearchTool = Tool.from_function(
    func=web_search,
    name="WebSearchTool",
    description=(
        "Use this tool when the user's question lacks sufficient background context "
        "or factual information that cannot be inferred from the conversation history. "
        "This tool performs a real web search via the Tavily API to gather the most recent, "
        "relevant, and factual data related to the query. "
        "It should typically be used after the ContextPresenceJudge indicates that context "
        "is missing or incomplete. "
        "Return only the most relevant factual text content (not metadata or links)."
    )
)
