import time
import random
import matplotlib.pyplot as plt

# Sorting algorithms
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Function to measure sorting time
def benchmark_sort(sort_fn, arr):
    start_time = time.time()
    sort_fn(arr)
    return time.time() - start_time

# Input sizes
input_sizes = [5, 10, 20, 100, 500, 1000, 5000, 10000]

# Benchmark each sorting algorithm
selection_times = []
insertion_times = []
bubble_times = []

for size in input_sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    
    # Time Selection Sort
    arr_copy = arr.copy()
    selection_times.append(benchmark_sort(selection_sort, arr_copy))
    
    # Time Insertion Sort
    arr_copy = arr.copy()
    insertion_times.append(benchmark_sort(insertion_sort, arr_copy))
    
    # Time Bubble Sort
    arr_copy = arr.copy()
    bubble_times.append(benchmark_sort(bubble_sort, arr_copy))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, selection_times, label='Selection Sort', marker='o')
plt.plot(input_sizes, insertion_times, label='Insertion Sort', marker='o')
plt.plot(input_sizes, bubble_times, label='Bubble Sort', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Benchmark: Selection Sort vs Insertion Sort vs Bubble Sort')
plt.legend()
plt.grid(True)
plt.show()
