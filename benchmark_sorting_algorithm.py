import timeit
import matplotlib.pyplot as plt

# Define the sorting algorithms

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

def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = i
        while array[current_value - 1] > array[current_value] and current_value > 0:
            array[current_value - 1], array[current_value] = array[current_value], array[current_value - 1]
            current_value -= 1
    return array

def selection_sort(array):
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# Function to measure the execution time of a sorting algorithm
def measure_time(sort_function, input_size):
    setup_code = f"from __main__ import {sort_function.__name__}"
    test_code = f"{sort_function.__name__}([i for i in range({input_size}, 0, -1)])"
    times = timeit.repeat(stmt=test_code, setup=setup_code, repeat=3, number=1)
    return min(times)  # Return the minimum time taken

# Define the range of input sizes for benchmarking
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

# Measure the time taken by each sorting algorithm for each input size
times_bubble = [measure_time(bubble_sort, size) for size in input_sizes]
times_insertion = [measure_time(insertion_sort, size) for size in input_sizes]
times_selection = [measure_time(selection_sort, size) for size in input_sizes]

# Plot the results using matplotlib
plt.plot(input_sizes, times_bubble, label='Bubble Sort', marker='o')
plt.plot(input_sizes, times_insertion, label='Insertion Sort', marker='o')
plt.plot(input_sizes, times_selection, label='Selection Sort', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Runtime of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.show()
