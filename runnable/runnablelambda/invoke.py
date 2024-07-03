# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 14:06
@Auth ： leon
"""
from langchain_core.runnables import RunnableLambda

def add_one(x:int)->int:
    return x+1
"""
1. 校验配置文件，如果没有传入配置文件，则初始化最小4个参数，
        empty = RunnableConfig(
        tags=[],
        metadata={},
        callbacks=None,
        recursion_limit=25,
    )
2. 根据config创建一个回调管理器
3. 利用回调管理器启动一个运行时的chain管理器
4. 如果fun函数是普通一次性返回的函数，则直接调用返回结果
5. 如果fun函数返回结果是一个迭代器，他也会将所有结果返回后拼接好，一次性返回
6. 如果fun返回的结果是一个runnable，则继续调用runnable的invoke，最大可递归深度为25
"""
runnable = RunnableLambda(add_one)
print(runnable.invoke(10))