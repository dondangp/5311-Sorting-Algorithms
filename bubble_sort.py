def bubble_sort(arr):
    n = len(arr) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        n -= 1
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output will be a sorted array: [11, 12, 22, 25, 34, 64, 90]
