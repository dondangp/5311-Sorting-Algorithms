def insertion_sort(array):
    # Iterate from the second element to the last element
    for i in range(1, len(array)):
        current_value = i
        
        # Shift elements of the sorted segment forward to make room for the element to be inserted
        while array[current_value - 1] > array[current_value] and current_value > 0:
            # Swap the elements to maintain the sorted order
            array[current_value - 1], array[current_value] = array[current_value], array[current_value - 1]
            current_value -= 1  # Move the current index back to continue checking
    
# Example usage:
arr = [2, 6, 5, 1, 3, 4]
insertion_sort(arr)
print(arr)  # Output will be a sorted array: [1, 2, 3, 4, 5, 6]
