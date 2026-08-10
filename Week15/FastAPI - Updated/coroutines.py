import asyncio

async def greet(name: str):
    return {"message": f"Hello! {name}"}

# This creates a coroutine object, but does not execute it yet
message = greet("John")
print(message)  # Output: <coroutine object greet at 0x000001D334F39930>
print(type(message))  # Output: <class 'coroutine'>

# To execute a coroutine, you need to await it within an async function or use an event loop
async def main():
    result = await greet("John")
    return result  # Output: {'message': 'Hello! John'}

# We can't directly run an async function without an event loop, so we use asyncio.run()
# Also asyncio.run() doesn't print the result, so we need to print it explicitly
output = asyncio.run(main())  # This will run the main coroutine and print the result
print(output) # Output: {'message': 'Hello! John'}

# We would also get a warning at the end
# sys:1: RuntimeWarning: coroutine 'greet' was never awaited
# It is because we created a coroutine object with variable 'message' but never awaited it. 
# To avoid this warning, we should either await the coroutine 
# or not create it at all if we don't intend to use it.
# So instead, result = await message in the main function instead of creating a separate variable.
