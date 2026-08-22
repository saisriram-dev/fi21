import asyncio


# ============================================================
# 1. ASYNC FUNCTION
# ============================================================
#
# "async def" defines an asynchronous function.
#
# Calling this function does NOT immediately execute all of
# its code.
#
# Instead:
#
#     download("A")
#
# creates a COROUTINE OBJECT.
#
# The coroutine can later be:
#
#     - awaited directly
#     - scheduled with asyncio.create_task()
#     - passed to asyncio.gather()
#
# ============================================================

async def download(name, seconds):
    print(f"{name}: started")

    # asyncio.sleep() is an asynchronous sleep.
    #
    # IMPORTANT:
    # This does NOT block the whole event loop.
    #
    # When we reach this await, this coroutine says:
    #
    #     "I have nothing to do for 'seconds' seconds.
    #      Event loop, you can run some other scheduled task."
    #
    await asyncio.sleep(seconds)

    print(f"{name}: finished")

    # This is the value that will eventually be returned
    # when somebody awaits this coroutine/task.
    return f"{name} result"


# ============================================================
# 2. ANOTHER ASYNC FUNCTION
# ============================================================

async def do_something_else():
    print("Other work: started")

    # Again, this coroutine temporarily gives control back
    # to the event loop.
    await asyncio.sleep(1)

    print("Other work: finished")

    return "Other work result"


# ============================================================
# 3. MAIN IS ALSO AN ASYNC FUNCTION
# ============================================================
#
# Because main() uses "await", main() itself must be an
# async function.
#
# ============================================================

async def main():

    print("\n--- PART 1: A COROUTINE OBJECT ---")

    # Calling an async function creates a coroutine object.
    #
    # IMPORTANT:
    # download("A", 3) does NOT mean "run download now".
    #
    # It creates a coroutine that describes the work.
    #
    coroutine_a = download("A", 3)

    print("Coroutine created.")

    # At this point, download() has NOT printed:
    #
    #     A: started
    #
    # because we haven't actually given the coroutine to
    # the event loop by awaiting it or scheduling it.


    print("\n--- PART 2: DIRECTLY AWAITING A COROUTINE ---")

    # Now we await the coroutine.
    #
    # This starts executing it.
    #
    # download() prints:
    #
    #     A: started
    #
    # Then it reaches:
    #
    #     await asyncio.sleep(3)
    #
    # At that point, download() pauses for 3 seconds.
    #
    # BUT:
    #
    # the event loop is NOT necessarily blocked.
    #
    # Other already-scheduled asynchronous tasks could run
    # during those 3 seconds.
    #
    # However, we have not created another task here.
    #
    # Therefore, from main()'s perspective, main is simply
    # waiting for A to finish.
    #
    result_a = await coroutine_a

    # We arrive here only after download("A", 3) has finished.
    print("Received:", result_a)


    print("\n--- PART 3: CREATE_TASK ---")

    # Now let's create a task.
    #
    # create_task() takes a coroutine and schedules it on
    # the event loop.
    #
    # IMPORTANT:
    #
    # create_task() does NOT mean:
    #
    #     "wait until this finishes."
    #
    # It means:
    #
    #     "Schedule this work to run independently while
    #      I continue doing other things."
    #
    task_b = asyncio.create_task(
        download("B", 3)
    )

    print("Task B has been scheduled.")

    # Notice that we have NOT written:
    #
    #     await task_b
    #
    # yet.
    #
    # So main() is free to continue.


    # We can schedule another task too.
    task_other = asyncio.create_task(
        do_something_else()
    )

    print("Other work has also been scheduled.")

    # At this point the event loop has multiple tasks available:
    #
    #     B
    #     Other work
    #
    # When main() reaches an await, the event loop can switch
    # between these tasks.


    print("\nMain is going to wait for B...")

    # Now we finally await task B.
    #
    # If B has already finished, this returns its result
    # immediately.
    #
    # If B has NOT finished, main() pauses here until B
    # finishes.
    #
    # Meanwhile, the event loop can continue running
    # "Other work".
    result_b = await task_b

    print("Received:", result_b)


    # We also need to get the result of the other task.
    result_other = await task_other

    print("Received:", result_other)


    print("\n--- PART 4: GATHER ---")

    # Instead of manually doing create_task() for every
    # coroutine, we can use asyncio.gather().
    #
    # gather() is useful when we want multiple asynchronous
    # operations to run concurrently and we want all of
    # their results.
    #
    # We give gather() the coroutine objects directly:
    #
    #     download("C", 3)
    #     download("D", 2)
    #
    # gather() takes care of scheduling/running them
    # concurrently.
    #
    # Then we await gather() because we want to wait until
    # BOTH operations are complete.
    #
    result_c, result_d = await asyncio.gather(
        download("C", 3),
        download("D", 2)
    )

    # C and D were allowed to run concurrently.
    #
    # C takes 3 seconds.
    # D takes 2 seconds.
    #
    # Therefore, the total waiting time is approximately
    # 3 seconds, NOT 5 seconds.
    #
    # Why?
    #
    # Because while C is waiting, D can run.
    #
    print("Received:", result_c)
    print("Received:", result_d)


# ============================================================
# 4. START THE ASYNC PROGRAM
# ============================================================
#
# asyncio.run() creates and manages the event loop and runs
# our main() coroutine.
#
# main() itself is a coroutine because we defined it with:
#
#     async def main()
#
# ============================================================

asyncio.run(main())
