from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
import os

def load_context_splitter_tool():
    template = """Split the following user input into two parts:
1. BACKGROUND CONTEXT
2. MAIN QUESTION

Return as:
Context: ...
Question: ...

User Input: {user_input}
"""
    prompt = PromptTemplate(input_variables=["user_input"], template=template)

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )

    chain = prompt | llm
    func=lambda x: chain.invoke({"user_input": x}).content


    tool = Tool(
        name="Context Splitter",
        func=lambda x: chain.run(user_input=x),
        description="Splits user input into background context and question."
    )
    return tool
