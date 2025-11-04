# 0-1 Knapsack Problem using Dynamic Programming (with user input)

def knapsack(weights, values, capacity):
    n = len(values)
    # Create DP table (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], 
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


# -------------------------------
# User Input Section
# -------------------------------
n = int(input("Enter number of items: "))

values = []
weights = []

print("\nEnter value and weight for each item:")
for i in range(n):
    v = int(input(f"  Value of item {i+1}: "))
    w = int(input(f"  Weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = int(input("\nEnter maximum capacity of knapsack: "))

# Solve and show result
max_value = knapsack(weights, values, capacity)
print("\nMaximum value that can be carried in knapsack =", max_value)
