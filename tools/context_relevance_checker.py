from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
import os


def load_context_relevance_tool():
    """
    Loads a tool that checks if the provided context is relevant to a user's question.
    Returns a LangChain Tool object.
    """
    template = """You are a context relevance evaluator.
Compare the following context with the user's question and determine
if the context is relevant to answering it.

Question: {question}
Context: {context}

Answer only "RELEVANT" or "NOT RELEVANT".
"""
    prompt = PromptTemplate(input_variables=["question", "context"], template=template)

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )

    chain = prompt | llm
    func=lambda inputs: chain.invoke(inputs).content


    tool = Tool(
        name="Context Relevance Checker",
        func=lambda inputs: chain.run(**inputs),
        description="Checks if the provided context is relevant to the user's question."
    )

    return tool
