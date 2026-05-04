from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_ollama import ChatOllama
from langchain_core.tools import tool

load_dotenv()

@tool
def triple(num:float) -> float:
    """parse the input and return the triple of the number"""
    return float(num * 3)


tools = [TavilySearch(max_results=1), triple]

llm = ChatOllama(model="gpt-oss", temperature=0).bind_tools(tools)



