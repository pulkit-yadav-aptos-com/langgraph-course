from dotenv import load_dotenv
from langgraph.graph import MessagesState, StateGraph, END, START
from langchain_core.messages import HumanMessage
from nodes import run_agent_reasoning, tool_node

import os

load_dotenv()
AGENT_REASONING = "agent_reasoning"
ACT = "act"
LAST = -1

def should_continue(state: MessagesState) -> str:
    if not state["messages"][LAST].tool_calls:
        return END
    return ACT


flow = StateGraph(MessagesState)


flow.add_node(AGENT_REASONING, run_agent_reasoning)
flow.set_entry_point(AGENT_REASONING)
flow.add_node(ACT, tool_node)

flow.add_conditional_edges(AGENT_REASONING, should_continue, {
    END:END,
    ACT:ACT})

flow.add_edge(ACT, AGENT_REASONING)
app = flow.compile()
app.get_graph().draw_mermaid_png(output_file_path="flow.png")

if __name__ == "__main__":
    print("Hello, World!")
    result = app.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo? List it and then triple it")]})
    print(result["messages"][LAST].content)