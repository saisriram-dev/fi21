nums = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in nums}
print(squares)

marks = {"ram": 45, "krishna": 82, "arjun": 67, "bheem": 90}
filtered = {name: value for name, value in marks.items() if value >= 70}
print(filtered)

words = ["python", "AI", "code", "data"]
lengths = {word: len(word) for word in words}
print(lengths)

d = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in d.items()}
print(swapped)

s = "banana"
freq = {ch: s.count(ch) for ch in set(s)}
print(freq)
