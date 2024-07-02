# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 14:06
@Auth ： leon
"""
from langchain_core.runnables import RunnableLambda
import asyncio
import time

def add_one(x:int)->int:
    return x+1
async def add_one_async(x: int) -> int:
    print('test-add-two-async')
    await asyncio.sleep(1)
    print(x)
    return x + 2
"""
1. 如果不指定参数，传入的参数默认给func
    1.1 如果传入的函数是异步的，则还会复制一份给afunc
2. 如果要直接传入afunc，则afunc必须是异步函数，且如果传入了afunc，就必须传入func，且func一定不能是异步
3. 当调用invoke时，执行的是func
4. 当调用ainvoke时，调用的是afunc
"""
runnable = RunnableLambda(func=add_one)
print(runnable.invoke(10))
print(asyncio.run(runnable.ainvoke(10)))

runnable = RunnableLambda(func=add_one,afunc=add_one_async)
print(runnable.invoke(10))
print(asyncio.run(runnable.ainvoke(10)))