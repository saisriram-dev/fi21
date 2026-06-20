Dynamic Programming (DP) is a **problem-solving technique** used in computer science and mathematics to solve complex problems by breaking them into **smaller overlapping subproblems**.

The key idea is:

> **Solve each small problem once, store the result, and reuse it later** instead of solving it again and again.

---

## Simple Example: Fibonacci Numbers

The Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13 ...

Each number is:

[
F(n) = F(n-1) + F(n-2)
]

F(n)=F(n-1)+F(n-2)

If we calculate `F(5)` normally:

- `F(5)` needs `F(4)` and `F(3)`
- `F(4)` again needs `F(3)` and `F(2)`
- `F(3)` gets calculated many times

This wastes time.

### Dynamic Programming Solution

Store already computed values:

```python
fib = [0, 1]

for i in range(2, 6):
    fib.append(fib[i-1] + fib[i-2])

print(fib[5])   # 5
```

Now each Fibonacci number is computed only once.

---

# Two Main Properties of DP

## 1. Overlapping Subproblems

The same smaller problems appear repeatedly.

Example:

- `F(3)` is calculated multiple times in recursion.

## 2. Optimal Substructure

The optimal solution can be built from optimal solutions of smaller problems.

---

# Two Common DP Methods

## 1. Memoization (Top-Down)

- Use recursion
- Save results in memory

```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

---

## 2. Tabulation (Bottom-Up)

- Start from smallest values
- Build answer step by step

```python
dp = [0, 1]

for i in range(2, n+1):
    dp.append(dp[i-1] + dp[i-2])
```

---

# Where Dynamic Programming Is Used

DP is commonly used in:

- Shortest path algorithms
- Knapsack problem
- Longest common subsequence
- Matrix chain multiplication
- Game strategies
- AI and optimization problems

---

# Easy Real-Life Analogy

Imagine climbing stairs:

- You can climb 1 or 2 steps at a time.
- To reach step 5, you can come from:
  - step 4
  - step 3

Instead of recalculating all ways repeatedly, you store the number of ways for each step.

That is dynamic programming.

---

# In One Sentence

> Dynamic Programming is an optimization technique where we solve smaller subproblems once, store their answers, and reuse them to efficiently solve bigger problems.
