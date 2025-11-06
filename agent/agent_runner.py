import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import tool
from tools.context_presence_judge import load_context_presence_tool
from tools.context_relevance_checker import load_context_relevance_tool
from tools.context_splitter import load_context_splitter_tool
from tools.web_search_tool import load_web_search_tool


load_dotenv()


@tool
def echo_tool(text: str) -> str:
    """Repeats what the user says."""
    return f"You said: {text}"


def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )


def load_tools():
    return [
        echo_tool,
        load_context_presence_tool(),
        load_context_relevance_tool(),
        load_context_splitter_tool(),
        load_web_search_tool(),
    ]


def create_executor():
    llm = get_llm()
    tools = load_tools()

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        input_key="input",
        return_messages=False
    )

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=3
    )
    return agent


def run_agent(user_input, session_memory=None):
    if session_memory:
        memory.chat_memory = session_memory

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )

    tools = [
        echo_tool,
        load_context_presence_tool(),
        load_context_relevance_tool(),
        load_context_splitter_tool(),
        load_web_search_tool()
    ]

    prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm, tools, prompt=prompt)

    executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=3
    )

    response = executor.invoke({"user_input": user_input})
    return response["output"], memory.chat_memory
