from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from tools.context_presence_judge import build_context_presence_tool
from tools.web_search_tool import build_web_search_tool
from dotenv import load_dotenv


load_dotenv()


llm = ChatOpenAI(model='gpt-4o', temperature=0.5)



contextJudgeTool = build_context_presence_tool(llm)
webSearchTool = build_web_search_tool()

tools = [contextJudgeTool, webSearchTool]


prompt = hub.pull("hwchase17/react")


agent = create_react_agent(llm, tools, prompt)


agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools,
    verbose = True, 
    handle_parsing_errors=True
)

print("--- Agent Executor has been initialized and is ready. ---")