import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
import datetime
from langchain.chat_models import ChatOpenAI

prompt = """
Translate the text delimited by triple backticks into a style that is {style}. 
text: ```{customer_email}```
"""

def get_response(prompt):
  chat = ChatOpenAI(model="gpt-3.5-turbo") 
  response = chat.complete(prompt)
  return response

response = get_response(prompt)
print(response)

