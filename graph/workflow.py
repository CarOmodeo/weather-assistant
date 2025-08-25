from langgraph.graph import StateGraph, START, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather import get_weather_by_location, get_weather_forecast
from model.llm_openai import create_llm_model



tools = [
    get_weather_by_location,
    get_weather_forecast
]

def invoke_llm(state: MessagesState):
    llm_openai = create_llm_model()
    llm_with_tools = llm_openai.bind_tools(tools, parallel_tool_calls=False)
    
    result = llm_with_tools.invoke(state['messages'])
    return {"messages": [result]}

def build_graph():

    builder = StateGraph(MessagesState)
    builder.add_node("invoke_llm",invoke_llm)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "invoke_llm")
    builder.add_conditional_edges("invoke_llm",tools_condition,)
    builder.add_edge("tools", "invoke_llm")

    return builder.compile()