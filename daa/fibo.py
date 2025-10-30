def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Enter a number: "))
print(f"Fibonacci({n}) =", fibonacci_recursive(n))

# Approach: Top-down (calls itself twice for each number)
# Time Complexity: O(2ⁿ) — each call branches into two more
# Space Complexity: O(n) — due to function call stack depth
# Advantages: Simple and easy to understand
# Disadvantages: Exponential time, redundant computations, stack overflow for large n

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input("Enter a number: "))
print(f"Fibonacci({n}) =", fibonacci_iterative(n))

# Approach: Bottom-up (uses loop and stores last two values)
# Time Complexity: O(n) — single loop runs n times
# Space Complexity: O(1) — only uses constant variables a and b
# Advantages: Fast, memory efficient
# Disadvantages: Less intuitive compared to recursion
