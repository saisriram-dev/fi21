import asyncio


async def fetch_user():
    # This coroutine simulates a slow network request.
    # While it is waiting at asyncio.sleep(), the event loop can run other tasks.
    await asyncio.sleep(3)

    # This is the value that this task will return.
    return "Alice"


async def fetch_orders():
    # This coroutine simulates another slow network request.
    await asyncio.sleep(5)

    # This task finishes after 5 seconds.
    return ["Order 1", "Order 2"]


async def fetch_recommendations():
    # This coroutine simulates a third independent operation.
    await asyncio.sleep(2)

    # This task finishes after 2 seconds.
    return ["Book", "Laptop"]


async def main():
    # TaskGroup creates a scope that manages all the tasks created inside it.
    # The tasks below are scheduled to run concurrently.
    async with asyncio.TaskGroup() as tg:

        # create_task() schedules fetch_user() to run as a separate task.
        # We keep the Task object so we can get its result later.
        user_task = tg.create_task(fetch_user())

        # This task starts concurrently with fetch_user().
        orders_task = tg.create_task(fetch_orders())

        # This task also starts concurrently with the other two.
        recommendations_task = tg.create_task(
            fetch_recommendations()
        )

    # Reaching this line means the TaskGroup has waited for all tasks
    # to finish successfully.
    # The TaskGroup does not leave the "async with" block until its tasks
    # are complete.

    # result() retrieves the value returned by the completed task.
    print(user_task.result())

    # This retrieves the list returned by fetch_orders().
    print(orders_task.result())

    # This retrieves the list returned by fetch_recommendations().
    print(recommendations_task.result())


# asyncio.run() creates the event loop and runs main().
asyncio.run(main())

# The important part is this:
#
# async with asyncio.TaskGroup() as tg:
#
#     tg.create_task(fetch_user())
#     tg.create_task(fetch_orders())
#     tg.create_task(fetch_recommendations())
#
#
# Instead of:
#
#     wait for user      → 3 seconds
#     wait for orders    → 5 seconds
#     wait for recommend → 2 seconds
#
# TaskGroup lets them make progress concurrently:
#
#     User:            |---------| 3s
#     Orders:          |-----------------| 5s
#     Recommendations: |------| 2s
#                      0       2    3    5
#
# Total time is approximately 5 seconds,
# because the three operations overlap.
#
#
# The other important feature of TaskGroup is failure handling.
#
# If one task raises an exception:
#
#     User:            |---------|
#     Orders:          |---ERROR-|
#     Recommendations: |---CANCEL|
#
# TaskGroup automatically cancels the remaining sibling tasks
# and waits for them to finish their cleanup.
#
# Therefore TaskGroup gives you:
#
#     1. Concurrent execution
#     2. Automatic task management
#     3. Sibling cancellation when one task fails
#     4. Waiting for all tasks and their cleanup
#     5. A clear boundary around related concurrent work
