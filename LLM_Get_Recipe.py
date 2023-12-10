#Deploy a Hugging face model using langchain and make function to use it
import sys
from langchain.prompts import PromptTemplate
sys.path.append('../..')
from langchain import HuggingFacePipeline
from transformers import AutoTokenizer, pipeline

# The model used is the recipe generation
model = "flax-community/t5-recipe-generation" 

# Initialize the tokenizer 
tokenizer = AutoTokenizer.from_pretrained(model)

# Create the pipeline
pipeline_recipe = pipeline(
  "text-generation",
  model=model,
  tokenizer=tokenizer,
  device=0
)
prompt_template_dishes="""
i want {dish_name} while having {ingridents} in {time}
"""

# Define a function that takes text as input and returns the generated output
def run_model_prompt(input_text):
  output = pipeline_recipe(input_text)[0]['generated_text']
  return output

def get_recipe(dish_name,ingridents,time):
  prompt = PromptTemplate.from_template(prompt_template_dishes)
  prompt.format(dish_name=dish_name, ingridents=ingridents,time=time)
  response = run_model_prompt(prompt)
  return response