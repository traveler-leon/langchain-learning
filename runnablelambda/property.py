# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 13:46
@Auth ： leon
"""
from langchain_core.runnables import RunnableLambda

b = 100
def add_one(x:int)->int:
    global b
    return x+1

runnable = RunnableLambda(add_one)

print(runnable.InputType)
print(runnable.OutputType)

# 比较的其实是内部的func和afunc
runnable1 = RunnableLambda(add_one)
print(runnable==runnable1)

print(str(runnable))