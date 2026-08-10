import asyncio

async def task1():
    await asyncio.sleep(2)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(1)
    return "Task 2 completed"

async def task3():
    await asyncio.sleep(3)
    return "Task 3 completed"

async def main():
    # Create a list of tasks
    tasks = [task1(), task2(), task3()]

    # Run the tasks concurrently and wait for them to complete
    # Gather tells asyncio to run all the tasks concurrently and wait for them to finish
    # So the flow is: first task2 will complete after 1 second, 
    # then task1 after 2 seconds, and finally task3 after 3 seconds
    # So total time taken will be 3 seconds, not 6 seconds
    res1, res2, res3 = await asyncio.gather(*tasks)

    return res1, res2, res3

if __name__ == "__main__":
    results = asyncio.run(main())
    print(results)
