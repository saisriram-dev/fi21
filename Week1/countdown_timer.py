# A countdown timer using for loop
import time

my_time = input("Enter the time in seconds for countdown: ")
for x in range(int(my_time), 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")
