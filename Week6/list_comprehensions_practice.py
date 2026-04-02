nums = [i for i in range(1, 11)]
squares_even = [num**2 for num in nums if num % 2 == 0]
print(squares_even)

words = ["hi", "hello", "world", "AI", "python"]
res = [word for word in words if len(word) > 3]
print(res)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 1.8) + 32 for c in celsius]
print(fahrenheit)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

nums = [1, 2, 3, 4, 5, 6]
label = ["even" if num % 2 == 0 else "odd" for num in nums]
print(label)

nums = [1, 2, 3, 4]
all_comb = [(x, y) for x in nums for y in nums]
print(all_comb)
