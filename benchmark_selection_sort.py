import timeit
import matplotlib.pyplot as plt

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

# Function to measure the execution time of the sorting algorithm
def measure_time(sort_function, input_size):
    setup_code = f"from __main__ import {sort_function.__name__}"
    test_code = f"{sort_function.__name__}([i for i in range({input_size}, 0, -1)])"
    times = timeit.repeat(stmt=test_code, setup=setup_code, repeat=3, number=1)
    return min(times)  # Return the minimum time taken

# Define the range of input sizes for benchmarking
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

# Measure the time taken by the selection sort for each input size
times_selection = [measure_time(selection_sort, size) for size in input_sizes]

# Plot the results using matplotlib
plt.plot(input_sizes, times_selection, label='Selection Sort', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Runtime of Selection Sort')
plt.legend()
plt.grid(True)
plt.show()
