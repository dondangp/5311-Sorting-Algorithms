import timeit
import matplotlib.pyplot as plt

def insertion_sort(array):
    # Iterate from the second element to the last element
    for i in range(1, len(array)):
        current_value = i
        
        # Shift elements of the sorted segment forward to make room for the element to be inserted
        while array[current_value - 1] > array[current_value] and current_value > 0:
            # Swap the elements to maintain the sorted order
            array[current_value - 1], array[current_value] = array[current_value], array[current_value - 1]
            current_value -= 1  # Move the current index back to continue checking

# Function to measure the execution time of the sorting algorithm
def measure_time(sort_function, input_size):
    setup_code = f"from __main__ import {sort_function.__name__}"
    test_code = f"{sort_function.__name__}([i for i in range({input_size}, 0, -1)])"
    times = timeit.repeat(stmt=test_code, setup=setup_code, repeat=3, number=1)
    return min(times)  # Return the minimum time taken

# Define the range of input sizes for benchmarking
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

# Measure the time taken by the insertion sort for each input size
times_insertion = [measure_time(insertion_sort, size) for size in input_sizes]

# Plot the results using matplotlib
plt.plot(input_sizes, times_insertion, label='Insertion Sort', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Runtime of Insertion Sort')
plt.legend()
plt.grid(True)
plt.show()
