# Function to solve 0-1 Knapsack Problem using Dynamic Programming
def knapsack(values, weights, capacity):
    number_of_items = len(values)

    # Create a 2D list (table) to store maximum value for each subproblem
    dp_table = []
    for i in range(number_of_items + 1):
        dp_table.append([0] * (capacity + 1))

    # Fill the table using bottom-up approach
    for item_index in range(1, number_of_items + 1):
        for current_capacity in range(1, capacity + 1):
            current_weight = weights[item_index - 1]
            current_value = values[item_index - 1]

            # If the item can fit in the current capacity
            if current_weight <= current_capacity:
                # Option 1: Include the item
                include_item = current_value + dp_table[item_index - 1][current_capacity - current_weight]

                # Option 2: Exclude the item
                exclude_item = dp_table[item_index - 1][current_capacity]

                # Take the better of the two options
                dp_table[item_index][current_capacity] = max(include_item, exclude_item)
            else:
                # If the item cannot fit, exclude it
                dp_table[item_index][current_capacity] = dp_table[item_index - 1][current_capacity]

    # The last cell of the table contains the maximum value
    return dp_table[number_of_items][capacity]


# ---------------- Main Program ----------------
print("0-1 Knapsack Problem using Dynamic Programming\n")

number_of_items = int(input("Enter the number of items: "))

values = []
weights = []

# Input values and weights of each item
for i in range(number_of_items):
    value = int(input(f"Enter the value of item {i + 1}: "))
    weight = int(input(f"Enter the weight of item {i + 1}: "))
    values.append(value)
    weights.append(weight)

# Input knapsack capacity
capacity = int(input("Enter the capacity of the knapsack: "))

# Function call
maximum_value = knapsack(values, weights, capacity)

# Output the result
print("\nThe maximum value that can be obtained =", maximum_value)
