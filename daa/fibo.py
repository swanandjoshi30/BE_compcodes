def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
num = int(input("Enter number: "))
print("Fibonacci Sequence(Recursive)")
for i in range(num + 1):
    print(fibonacci_recursive(i),end=" ")
# Time Complexity: O(2ⁿ)
# Space Complexity:O(n)


def fibonacci_iterative(n):
    print("Fibonacci Sequence(Iterative):")
    a, b = 0, 1
    print(a,end=" ")
    for _ in range(n):
        print(b, end = " ")
        a, b = b, a + b
num = int(input("Enter number: "))
fibonacci_iterative(num)
# Time Complexity: O(n)
# Space Complexity:O(1)
