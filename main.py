from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
from graph.workflow import build_graph

load_dotenv()


messages = [
    SystemMessage(content="""
    You are a weather assistant. Your tasks are:
    - Return the current weather in a given location
    - Return the weather forecast for a number of days in a given location
    
    General Rules:
    - You must not answer questions that are not related to your tasks
    - Always answer with a single sentence
    """)
]

agent = build_graph()

print("🌤️ Welcome to the weather assistant.\n")
print("Ask the assistant (type 'exit' to close the application)")

while True:
    user_input = input("\n🧑 You: ")
    
    if user_input.strip().lower() in {"exit", "salir", "quit"}:
        print("👋 ¡Bye Bye!")
        break

    try:
        response = agent.invoke({"messages": [HumanMessage(content=user_input)]})
        ai_message = response["messages"][-1]
        print(f"🤖 Assistant: {ai_message.content}")
    
    except Exception as e:
        print("❌ There was an error when processing your request:", str(e))



