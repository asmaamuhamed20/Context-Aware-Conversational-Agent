from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
import os

def load_context_presence_tool():
    template = """Determine if the user input provides enough context to answer a question.
Answer ONLY 'YES' or 'NO'.

Question: {input}
"""
    prompt = PromptTemplate.from_template(template)

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )

    chain = prompt | llm

    def check_context(input_text):
        return chain.invoke({"input": input_text}).content

    tool = Tool(
        name="ContextPresenceJudge",
        func=check_context,
        description="Determines if the user's input has enough context to answer."
    )
    return tool
