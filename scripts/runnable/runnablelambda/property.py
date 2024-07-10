# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 13:46
@Auth ： leon
"""
from langchain_core.runnables import RunnableLambda

b = 100
def add_one(x):
    global b
    return x+1

def add_one_int(x:int)->int:
    return x+1

runnable = RunnableLambda(add_one)
print(runnable.InputType)
print(runnable.OutputType)
# 如果不明确写出参数数据类型，将被视为任何数据类型Any
runnable_int = RunnableLambda(add_one_int)
print(runnable_int.InputType)
print(runnable_int.OutputType)
print(runnable_int.input_schema.dict)
print(runnable_int.input_schema.schema_json.__annotations__)
# for i in runnable_int.input_schema.dict:
#     pri
print(runnable_int.output_schema.schema.__annotations__)







# 比较的其实是内部的func和afunc
runnable1 = RunnableLambda(add_one)
print(runnable==runnable1)

print(str(runnable))