import re

from langchain.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph

from model import llm
from news_state import AnalyzeResult, ArticleSchema, NewsState
from tools.fetch_news import search_news

SYS_PROMPT = "" \
"角色：你是一个新闻总结助手，" \
"任务：请你根据一下文章总结标题，并结合用户输入的关键词，选出你觉得合适的3篇文章"

def search_node(state:NewsState):
    """搜集热点新闻节点"""
    news_list = search_news(state['user_input'])
    return {"articles":news_list}

def analyze_node(state:NewsState):
    """ai总结节点"""
    structured_llm = llm.with_structured_output(AnalyzeResult,method = "function_calling")
    result = structured_llm.invoke([
        SystemMessage(content=SYS_PROMPT),
        HumanMessage(content=f"用户关键词：{state['user_input']}。'\n'文章信息：{state['articles']}")
    ])
    return  {"analyze" : result}

def write_node(state:NewsState):
    """写入节点"""
    result = state["analyze"]
    for article in result.analyze:
        print(f"文章展示:{article}\n")
        
    return {}

builder  = StateGraph(NewsState)
builder.add_node("search",search_node)
builder.add_node("analyze",analyze_node)
builder.add_node("write",write_node)
builder.add_edge(START,"search")
builder.add_edge("search","analyze")
builder.add_edge("analyze","write")
builder.add_edge("write",END)

graph = builder.compile()

result = graph.invoke({"user_input":"ai"})
