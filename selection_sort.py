def selection_sort(array):
    # Iterate over each element in the array except the last one
    for i in range(0, len(array) - 1):
        # Assume the current element is the smallest
        min_index = i
        
        # Iterate through the unsorted portion of the array
        for j in range(i + 1, len(array)):
            # If a smaller element is found, update min_index
            if array[j] < array[min_index]:
                min_index = j
                
        # Swap the smallest found element with the first element of the unsorted portion
        array[i], array[min_index] = array[min_index], array[i]

# Example usage
# array = [64, 25, 12, 22, 11]
# selection_sort(array)
# print("Sorted array:", array)
