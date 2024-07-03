# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 14:06
@Auth ： leon
"""
from langchain_core.runnables import RunnableLambda

def add_one(x:int)->int:
    return x+1
"""
1. 校验配置文件
    1.1.如果没有传入配置文件，则初始化最小4个参数，
        empty = RunnableConfig(
        tags=[],
        metadata={},
        callbacks=None,
        recursion_limit=25,
    )
    1.2. 如果输入是多个，则配置文件要copy到同样长度，得到一个配置文件列表
    1.3. 配置文集列表中只有第一个要设置run_id,其他的需要删除，便于trace追踪
    
2. 创建一个线程池，并行调用invoke
"""
runnable = RunnableLambda(add_one)
print(runnable.batch([10,32]))