from langgraph.graph import StateGraph, START,END
from typing import TypedDict,Annotated,Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.messages import HumanMessage, SystemMessage,BaseMessage
from langgraph.graph.message import add_messages
import operator
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.memory import MemorySaver #saves in RAM memory
load_dotenv(dotenv_path='F:\\agentic_ai\\AgenticAIWorkspace\\.env')

llm = ChatOpenAI()

class ChatState(TypedDict):
    messages = Annotated[list[BaseMessage],add_messages]

def chat_node(state:ChatState):
    messages = state['messages']
    response = llm.invoke(messages).content
    return {'messages':[response]}

#greph

checkpointer = InMemorySaver()
graph = StateGraph(ChatState)

# add node
graph.add_node('chat_node',chat_node)

# add edge
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)
chatbot = graph.compile(checkpointer=checkpointer)
