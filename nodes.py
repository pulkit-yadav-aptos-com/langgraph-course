from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools
load_dotenv()

SYSTEM_MESSAGE = """
You are a helpful assistant that can use tools to answer questions
For tavily_search, only pass query unless the user explicitly asks for a time window; never set time_range together with start_date or end_date."""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """Run the agent reasoning"""

    messages = [{"role": "system", "content": SYSTEM_MESSAGE.strip()}, *state["messages"]]
    response = llm.invoke(messages)
    return {"messages": [response]}


tool_node = ToolNode(tools)

