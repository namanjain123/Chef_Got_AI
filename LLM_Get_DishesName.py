import os
import openai
import sys
from langchain.prompts import PromptTemplate
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
import datetime
from langchain.chat_models import ChatOpenAI

prompt_template_dishes = """
[Role]
Act as a Chef Assitant who follow the steps and gives results at the end gives dishes name with their brief in JSON
[Steps]

Step 1 : Understand the Given Ingrident
Step 2 : Undrstand the Given Cusine , Mood and Time Span avalabile
Step 3 : According to all the Above Factors Suggest Dishes for the number of people such that least amount of ingrident are used while providing best taste and nutrition value to satify meal for {person_number} person.
Step 4 : Make atleast 7 Dishes suggestion with basic info that would be needed.
[Steps End]

Ingrident List : ``` {ingrident_list} ``` 
Motivation : ```{motivation}``` 
Result: ```
"""
prompt_template_dsihes="""
[Role]
You are a assitant that make use of Master Details and Pointers and the Time to make a small note about his motivation of food using his body details , what meal he is having and the pointers into less then 50 word
Master Details : ```{master_details}```
Pointer: ```{pointer}```

"""
chat = ChatOpenAI(model="gpt-3.5-turbo")
def get_Dishes_option(ingrident,motivation):
  prompt = PromptTemplate.from_template(prompt_template_dishes)
  prompt.format(ingrident_list=ingrident, motivation=motivation)
  response = chat.complete(prompt)
  return response

def get_Motivation(details,pointers):
  prompt = PromptTemplate.from_template(prompt_template_dsihes)
  prompt.format(master_details=details, pointer=pointers)
  response = chat.complete(prompt)
  return response

# Now we will chain them both in easy fashion
from langchain import SequentialChain
def chained_get_Dishes_option(ingrident,details,pointers):

  chain = SequentialChain()

  # Add get_Motivation function to chain
  chain.add_step(get_Motivation, 
                  details=details, 
                  pointers=pointers)
  # Capture output of get_Motivation  
  motivation = chain.run()[-1] 
  # Add get_Dishes_option function to chain 
  chain.add_step(get_Dishes_option,
                  ingrident=ingrident,
                  motivation=motivation)

  # Run the chain
  response = chain.run()
  return response

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