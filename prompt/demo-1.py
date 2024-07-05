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
prompt_1 = prompt_template.invoke({"topic":"cats"})
print(prompt_1)

prompt_2 = prompt_template.invoke("cats")
print(prompt_2)