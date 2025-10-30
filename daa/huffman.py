import heapq   # Used to create a priority queue (min-heap)

# Function to generate Huffman codes
def huffman_encoding(frequency):
    heap = []
    
    # Step 1: Create a heap with [frequency, [character, code]]
    for character, freq in frequency.items():
        heap.append([freq, [character, ""]])
    
    heapq.heapify(heap)   # Convert list into a min-heap
    
    # Step 2: Combine two smallest nodes until one remains
    while len(heap) > 1:
        smallest1 = heapq.heappop(heap)
        smallest2 = heapq.heappop(heap)
        
        # Add '0' to the code of the first smallest
        for pair in smallest1[1:]:
            pair[1] = "0" + pair[1]
        
        # Add '1' to the code of the second smallest
        for pair in smallest2[1:]:
            pair[1] = "1" + pair[1]
        
        # Merge them into a new node
        new_node = [smallest1[0] + smallest2[0]] + smallest1[1:] + smallest2[1:]
        heapq.heappush(heap, new_node)
    
    # Step 3: Extract the codes from the final heap
    result = heapq.heappop(heap)[1:]
    result.sort(key=lambda p: (len(p[1]), p))   # Sort for neat output
    return result

# -------- Main Program --------
text = input("Enter a text: ")

# Step 1: Count the frequency of each character
frequency = {}
for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

# Step 2: Generate Huffman codes
codes = huffman_encoding(frequency)

# Step 3: Display results
print("\nCharacter | Frequency | Huffman Code")
print("------------------------------------")
for item in codes:
    character = item[0]
    code = item[1]
    print("   '{}'\t      {}\t\t{}".format(character, frequency[character], code))

# Total Time Complexity		O(n + k log k)
# Space Complexity		O(k)
