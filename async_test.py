# -*- coding: utf-8 -*-
"""
@Time ： 2024/7/1 10:51
@Auth ： leon
"""
import asyncio

async def task1():
    print("Start task1")
    await asyncio.sleep(2)
    print("End task1")

async def task2():
    print("Start task2")
    await asyncio.sleep(1)
    print("End task2")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
