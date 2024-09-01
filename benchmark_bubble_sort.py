import timeit
import matplotlib.pyplot as plt

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

# Function to measure the execution time of the sorting algorithm
def measure_time(sort_function, input_size):
    setup_code = f"from __main__ import {sort_function.__name__}"
    test_code = f"{sort_function.__name__}([i for i in range({input_size}, 0, -1)])"
    times = timeit.repeat(stmt=test_code, setup=setup_code, repeat=3, number=1)
    return min(times)  # Return the minimum time taken

# Define the range of input sizes for benchmarking
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

# Measure the time taken by the bubble sort for each input size
times_bubble = [measure_time(bubble_sort, size) for size in input_sizes]

# Plot the results using matplotlib
plt.plot(input_sizes, times_bubble, label='Bubble Sort', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Runtime of Bubble Sort')
plt.legend()
plt.grid(True)
plt.show()
