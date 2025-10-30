import random
import time

# Function to perform partition (Deterministic)
def deterministic_partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


# Function for Deterministic Quick Sort
def deterministic_quick_sort(array, low, high):
    if low < high:
        partition_index = deterministic_partition(array, low, high)
        deterministic_quick_sort(array, low, partition_index - 1)
        deterministic_quick_sort(array, partition_index + 1, high)


# Function to perform partition (Randomized)
def randomized_partition(array, low, high):
    random_index = random.randint(low, high)
    array[random_index], array[high] = array[high], array[random_index]
    return deterministic_partition(array, low, high)


# Function for Randomized Quick Sort
def randomized_quick_sort(array, low, high):
    if low < high:
        partition_index = randomized_partition(array, low, high)
        randomized_quick_sort(array, low, partition_index - 1)
        randomized_quick_sort(array, partition_index + 1, high)


# ---------------- Main Program ----------------
print("Quick Sort Analysis (Deterministic and Randomized)\n")

number_of_elements = int(input("Enter the number of elements: "))
input_array = []

for i in range(number_of_elements):
    element = int(input(f"Enter element {i + 1}: "))
    input_array.append(element)

# Copy arrays for fair comparison
array_deterministic = input_array.copy()
array_randomized = input_array.copy()

# --- Deterministic Quick Sort ---
start_time = time.time()
deterministic_quick_sort(array_deterministic, 0, number_of_elements - 1)
end_time = time.time()
deterministic_time = end_time - start_time

# --- Randomized Quick Sort ---
start_time = time.time()
randomized_quick_sort(array_randomized, 0, number_of_elements - 1)
end_time = time.time()
randomized_time = end_time - start_time

# Display sorted arrays and timing results
print("\nSorted array using Deterministic Quick Sort:")
print(array_deterministic)

print("\nSorted array using Randomized Quick Sort:")
print(array_randomized)

print("\n--- Time Analysis ---")
print("Deterministic Quick Sort Time:", deterministic_time, "seconds")
print("Randomized Quick Sort Time:", randomized_time, "seconds")
