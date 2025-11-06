# main.py
from agent.agent_runner import run_agent

def cli_loop():
    print("=== A Context-Aware Conversational Agent — CLI Test ===")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("\nUser: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        try:
            response = run_agent(user_input)
        except Exception as e:
            response = f"Error running agent: {e}"
        print("\nAgent:", response)

if __name__ == "__main__":
    cli_loop()
