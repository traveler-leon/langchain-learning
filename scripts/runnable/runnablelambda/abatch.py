# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 14:06
@Auth ： leon
"""
from langchain_core.runnables import RunnableLambda
import asyncio
import time

async def add_one_async(x: int) -> int:
    print('test-add-one-async')
    await asyncio.sleep(1)
    print(x)
    return x + 1
async def add_two_async(x: int) -> int:
    print('test-add-two-async')
    time.sleep(1)
    print(x)
    return x + 2
"""
1. 启动一个协程
2. 异步调用协程函数
3. 
"""
runnable_one = RunnableLambda(add_one_async)
runnable_two = RunnableLambda(add_two_async)

asyncio.run(runnable_one.abatch([10,23,34]))