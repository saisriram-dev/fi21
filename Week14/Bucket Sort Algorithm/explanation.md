**Bucket Sort** is a sorting algorithm that works by dividing elements into several buckets based on their value range. Each bucket stores elements that fall within a specific interval. The elements inside each bucket are sorted individually, often using a simple algorithm like insertion sort, and then all the buckets are merged in order to obtain the final sorted list. Bucket sort is highly efficient for data that is uniformly distributed over a known range, with an average time complexity of **O(n + k)**, where _n_ is the number of elements and _k_ is the number of buckets.

**Example:**

Consider the array:

**[29, 25, 3, 49, 9, 37, 21, 43]**

Create 5 buckets for the ranges:

- Bucket 1 (0 to 9): **[3, 9]**
- Bucket 2 (10 to 19): **[]**
- Bucket 3 (20 to 29): **[29, 25, 21]**
- Bucket 4 (30 to 39): **[37]**
- Bucket 5 (40 to 49): **[49, 43]**

Sort each bucket:

- **[3, 9]**
- **[]**
- **[21, 25, 29]**
- **[37]**
- **[43, 49]**

Merge the buckets:

**[3, 9, 21, 25, 29, 37, 43, 49]**

This is the final sorted array. Bucket sort performs best when the input values are spread evenly across the buckets.
