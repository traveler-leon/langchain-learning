# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/3 14:17
@Auth ： leon
"""
from langchain_core.prompts import PromptTemplate
"""
1. 
"""
prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")
prompt = prompt_template.invoke({"topic":"cats"})
print(prompt_template)
print(type(prompt_template))
print(prompt)
print(type(prompt))
print(prompt_template.input_schema.)