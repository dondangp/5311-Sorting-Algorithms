# Sorting Algorithms

This repository highlights three classic sorting algorithms: **Selection Sort**, **Insertion Sort**, and **Bubble Sort**. It includes both the implementation code for these algorithms and benchmark scripts to measure their performance on different input sizes.

## Benchmark - Sorting Algorithms
### Benchmark Environment

- **Operating System**: macOS 14.4.1 (23E224)
- **Processor/Chip**: Apple M2 (8-core CPU)
- **Clock Speed**: Up to 3.49 GHz
- **RAM**: 8 GB
- **Storage**: 245.11 GB Macintosh HD
- **Python Version**: 3.12.0
- **Virtual Environment**: Yes (`venv`)
- **Major Dependencies**: `timeit`, `matplotlib`
- **Device Power Status**: Plugged in
- **Background Processes**: Minimal activity, no significant CPU load during benchmarking.

### Benchmark
![sorting_algorithms_benchmark](https://github.com/user-attachments/assets/3faa44e3-fe7f-41be-9cda-e2265546a21a)
## Selection Sort Correctness

Selection Sort is an algorithm that sorts an array by repeatedly finding the minimum element from the unsorted portion of the array and swapping it with the first unsorted element. This process is repeated until the entire array is sorted. We can prove the correctness of Selection Sort using the concept of a **loop invariant**.

### Loop Invariant

**Invariant**: At the start of each iteration of the outer loop (with index `i`), the subarray `array[0..i-1]` consists of the `i` smallest elements in the array, sorted in non-decreasing order, and the subarray `array[i..n-1]` contains the remaining unsorted elements.

### Proof by Induction

I will prove the correctness of Selection Sort by demonstrating that the loop invariant holds at three crucial points: **Initialization**, **Maintenance**, and **Termination**.

#### 1. Initialization

Before the first iteration of the loop (`i = 0`), the subarray `array[0..i-1]` is empty. An empty subarray trivially satisfies the loop invariant, as it contains zero elements that are correctly sorted.

#### 2. Maintenance

Assume that before the `i`-th iteration, the loop invariant holds: the subarray `array[0..i-1]` is sorted and contains the `i` smallest elements in the array.

During the `i`-th iteration:
- The algorithm scans the unsorted portion of the array `array[i..n-1]` to find the smallest element.
- It swaps this smallest element with the element at `array[i]`, thereby extending the sorted subarray by one element.

After this swap, the subarray `array[0..i]` now contains the `i+1` smallest elements of the entire array, sorted in non-decreasing order, which maintains the loop invariant.

#### 3. Termination

The loop terminates when `i = n-1`. At this point, the loop invariant guarantees that the subarray `array[0..n-2]` is sorted and contains the `n-1` smallest elements in the array. The final element, `array[n-1]`, is already the largest element and is in its correct position.

Thus, upon termination, the entire array `array[0..n-1]` is sorted in non-decreasing order.

### Conclusion

By the principle of mathematical induction, the loop invariant holds for every iteration of the loop. Therefore, Selection Sort correctly sorts the array.

This proof demonstrates that Selection Sort is a correct sorting algorithm that will always produce a sorted array for any input.

## **Environment Setup**

### 1. Install Python
Ensure that Python 3.12.0 (or later) is installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

### 2. Set Up Your Environment
To install the necessary dependencies, follow these steps:

1. **Open your terminal**.

2. **Install the required Python packages** by running the following commands:
   ```sh
   pip install timeit
   pip install matplotlib
