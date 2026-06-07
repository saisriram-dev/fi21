A hash map is a data structure that stores data as key-value pairs and provides very fast lookup, insertion,
and deletion operations.

The reason it's fast is that it uses a hash function to convert a key into an array index (called a bucket),
allowing it to jump directly to where the data is stored instead of searching through all elements.

For example:
Index: 0 1 2 3 4 5 6 7 8 9
Value: [_ _ _ _ _ _ _ _ _ _]

Suppose we want to store:
Key = 27
Value = "Apple"

We use a hash function:
hash(key) = key % 10
So: intial 27 -> 27 % 10 = 7 and the value 'Apple' get's stored in index 7
Index: 0 1 2 3 4 5 6 7 8 9
Value: [_ _ _ _ _ _ _ Apple _ _]

So, if we want to access the value corresponding to 27:
get(27) -> hash(27) = 27 % 10 = 7 -> Value(7) == Apple [O(1)]
