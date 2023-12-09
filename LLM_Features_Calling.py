import os
import openai
import sys
from langchain.prompts import PromptTemplate
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
import datetime
from langchain.chat_models import ChatOpenAI

prompt_template = """
[Role]
Act as a Chef Assitant who follow the steps and gives results at the end gives only dishes name in JSON
[Steps]

Step 1 : Understand the Given Ingrident
Step 2 : Undrstand the Given Cusine , Mood and Time Span avalabile
Step 3 : According to all the Above Factors Suggest Dishes for the number of people such that least amount of ingrident are used while providing best taste and nutrition value to satify meal for {person_number} person.
Step 4 : Make atleast 7 Dishes suggestion with basic info that would be needed.
[Steps End]

Ingrident List : ``` {ingrident_list} ``` 
Motivation : ```{motivation}``` 
"""

def get_response(ingrident,motivation):
  chat = ChatOpenAI(model="gpt-3.5-turbo")
  prompt = PromptTemplate.from_template(prompt)
  prompt.format(ingrident_list=ingrident, motivation=motivation)
  response = chat.complete(prompt)
  return response

response = get_response()
print(response)



# Sample 

# [Role]
# Act as a Chef Assitant who follow the steps and gives results at the end gives only dishes name in JSON
# [Steps]

# Step 1 : Understand the Given Ingrident List
# Step 2 : Undrstand the Given Cusine , Mood and Time Span avalabile
# Step 3 : According to all the Above Factors Suggest Dishes for the number of people such that least amount of ingrident are used while providing best taste and nutrition value to satify meal for 2 person.
# Step 4 : Make atleast 5 Dishes suggestion with basic info that would be needed

# [Steps End]
# ``` 
# Ingrident List : {
#   "spices": [
#     "Turmeric",
#     "Cumin",
#     "Coriander",
#     "Garam Masala",
#     "Red Chili Powder",
#     "Cinnamon"
#   ],
#   "legumes": [
#     "Chickpeas",
#     "Lentils (any variety)"
#   ],
#   "grains": [
#     "Rice (Basmati or any preferred variety)",
#     "Wheat Flour (for making rotis/chapatis)"
#   ],
#   "condiments": [
#     "Ghee (clarified butter)",
#     "Vegetable Oil"
#   ],
#   "vegetables": [
#     "Onions",
#     "Tomatoes",
#     "Potatoes",
#     "Green Peas",
#     "Bell Peppers",
#     "Spinach"
#   ],
#   "protein": [
#     "Chicken",
#     "Paneer (Indian cottage cheese)"
#   ],
#   "dairy": [
#     "Yogurt"
#   ],
#   "others": [
#     "Salt",
#     "Sugar",
#     "Fresh Coriander Leaves (Cilantro)"
#   ]
# }

# Motivation: i want a nice warm veg dinner for Indian cuisine with Mexican twist and have a focus on protein and want to focus on taste and have very little time. ```

# Result
