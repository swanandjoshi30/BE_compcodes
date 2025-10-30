# Function to solve Fractional Knapsack problem
def fractional_knapsack(weights, values, capacity):
    n = len(values)
    
    # Create a list of items with value, weight, and ratio
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append([values[i], weights[i], ratio])
    
    # Sort items by ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0  # Total value accumulated in knapsack
    remaining_capacity = capacity
    
    # Pick items one by one
    for item in items:
        value = item[0]
        weight = item[1]
        
        if remaining_capacity >= weight:
            # Take the full item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of the item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
            break  # Knapsack is full
    
    return total_value


# -------- Main Program --------
n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    val = float(input(f"Enter value of item {i+1}: "))
    wt = float(input(f"Enter weight of item {i+1}: "))
    values.append(val)
    weights.append(wt)

capacity = float(input("Enter capacity of knapsack: "))

# Call function
max_value = fractional_knapsack(weights, values, capacity)

print("\nMaximum value that can be obtained =", max_value)

# Total Time Complexity		O(n log n)
# Space Complexity		O(n)
