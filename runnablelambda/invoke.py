# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 14:06
@Auth ： leon
"""
from langchain_core.runnables import RunnableLambda

def add_one(x:int)->int:
    return x+1

runnable = RunnableLambda(add_one)
