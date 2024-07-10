# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 13:34
@Auth ： leon
"""
import inspect
from inspect import Signature
def func(a:str,b:str)->str:
    """hello world"""
    return "hello"+str(a+b)
sig = inspect.signature(func)
print(sig)
print(type(sig))
print(sig.parameters)
print(sig.return_annotation)

sor = inspect.getsource(func)

print(sor)