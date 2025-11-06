from langchain.tools import Tool
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

import wikipedia

def load_web_search_tool():
    """Loads a web search tool using Wikipedia search."""
    def search_wikipedia(query):
        try:
            return wikipedia.summary(query, sentences=3)
        except Exception as e:
            return f"No relevant data found. ({e})"

    tool = Tool(
        name="Web Search Tool",
        func=search_wikipedia,
        description="Retrieves relevant information using Wikipedia search."
    )
    return tool
