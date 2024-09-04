def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
# Example use
arr = [2, 6, 5, 1, 3, 4]
insertion_sort(arr)
print(arr) 
