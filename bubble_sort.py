def bubble_sort(arr):
    # Calculate the number of passes needed (length of the array minus 1)
    n = len(arr) - 1
    is_sorted = False  # Boolean flag to check if the list is sorted

    # Continue looping until the array is sorted
    while not is_sorted:
        is_sorted = True  # Assume the array is sorted at the start of each pass
        
        # Traverse through the array
        for i in range(n):
            # If the current element is greater than the next element, swap them
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False  # Set the flag to False since a swap occurred

        # Reduce the length of the array to check as the last element in each pass is in its correct position
        n -= 1

    return arr  # Return the sorted array

# Example usage:
# arr = [64, 34, 25, 12, 22, 11, 90]
# sorted_arr = bubble_sort(arr)
# print(sorted_arr)  # Output will be a sorted array: [11, 12, 22, 25, 34, 64, 90]
