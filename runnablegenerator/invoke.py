# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/2 15:40
@Auth ： leon
"""
from typing import Any,AsyncIterator,Iterator
from langchain_core.runnables import RunnableGenerator
def gen(input:Iterator[Any])->Iterator[str]:
    for token in ["Have","a","nice","day"]:
        yield token

runnable = RunnableGenerator(gen)
# print(runnable.invoke(None))
for i in runnable.stream(None):
    print(i)