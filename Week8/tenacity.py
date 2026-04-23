from tenacity import retry, stop_after_attempt, wait_exponential


# Retry function use
# @retry is a decorator that retries the function if it fails
@retry
def risky_operation():
    # Your code here
    pass


# Other parameters
# stop_after_attempt: Number of attempts to stop after
# wait_exponential: Wait time between attempts

"""
    Example with parameters:
    The below code will retry the function 3 times with exponential backoff
    The exponential backoff means the wait time will increase exponentially
    In this case, the wait time will be 4, 8, 16 seconds
    Multiplier is the factor by which the wait time will be multiplied
    Min is the minimum wait time
    Max is the maximum wait time
    In this case the maximum wait time is 10 seconds
    So the wait time sequence will be 4, 8, 10 (capped at max)
"""


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def risky_operation():
    # Your code here
    pass
