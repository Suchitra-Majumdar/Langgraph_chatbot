from langgraph.graph import StateGraph, START,END
from typing import TypedDict,Annotated,Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from langchain_core.messages import HumanMessage, SystemMessage,BaseMessage
from langgraph.graph.message import add_messages
import operator
from langgraph.checkpoint.memory import MemorySaver #saves in RAM memory
load_dotenv(dotenv_path='F:\\agentic_ai\\AgenticAIWorkspace\\.env')

