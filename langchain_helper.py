import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openAI_key
import streamlit as st

os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]


llm = OpenAI(temperature=0.7) #temperature,how creative your model to be. ranges b/w 0 and 1. 0 not risky,very simple...1 risky and very creative


def generator_resturant_name_items(cuisine):
    
    llm = OpenAI(temperature=0.7)
    prompt_template_name = PromptTemplate(
                       input_variables = ['cuisine'],
                       template = "I want to open a resturant for {cuisine} food.Suggest a fancy name for this")

    name_chain = LLMChain(llm=llm,prompt=prompt_template_name,output_key='resturant_name')


    llm = OpenAI(temperature=0.7)
    prompt_template_items = PromptTemplate(
                        input_variables = ['resturant_name'],
                        template = "Suggest some menu items for {resturant_name}. Return it as a comma separated value")
        
    food_items_chain = LLMChain(llm=llm,prompt=prompt_template_items,output_key='menu_items')

    chain = SequentialChain(
        chains = [name_chain,food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['resturant_name','menu_items']
    )

    response = chain({"cuisine":cuisine})

    return response

if __name__ == "__main__":
    print(generator_resturant_name_items("Indian"))
