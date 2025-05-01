import random
import time
from concurrent.futures import ThreadPoolExecutor

def partition(arr, low, high):  
    """Partition the array using a random pivot."""
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort_sequential(arr, low, high):
    """Standard single-threaded quicksort."""
    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort_sequential(arr, low, pivot_idx - 1)
        quicksort_sequential(arr, pivot_idx + 1, high)

class QuickSortMultiThreading:
    """
    Multithreaded quicksort with depth control.
    
    Args:
        arr: List to sort.
        max_depth: Recursion depth limit for parallelism.
    """
    def __init__(self, arr, max_depth=3):
        self.arr = arr
        self.max_depth = max_depth

    def quicksort(self, low, high, depth=0):
        if low < high:
            pivot_idx = partition(self.arr, low, high)

            if depth < self.max_depth:
                with ThreadPoolExecutor(max_workers=2) as executor:
                    left = executor.submit(self.quicksort, low, pivot_idx - 1, depth + 1)
                    right = executor.submit(self.quicksort, pivot_idx + 1, high, depth + 1)
                    left.result()
                    right.result()
            else:
                self.quicksort(low, pivot_idx - 1, depth + 1)
                self.quicksort(pivot_idx + 1, high, depth + 1)

    def sort(self):
        self.quicksort(0, len(self.arr) - 1)

def run_performance_test():
    """Compare performance of sequential and multithreaded quicksort."""
    array_sizes = [10000, 100000, 1000000]

    print("Performance Comparison: Sequential vs Parallel Quicksort")
    print("-" * 60)
    print(f"{'Array Size':<15} {'Sequential (ms)':<20} {'Parallel (ms)':<20} {'Speedup':<10}")
    print("-" * 60)

    for size in array_sizes:
        random.seed(42)
        arr1 = [random.randint(0, size) for _ in range(size)]
        arr2 = arr1.copy()

        start = time.time()
        quicksort_sequential(arr1, 0, len(arr1) - 1)
        seq_time = (time.time() - start) * 1000

        sorter = QuickSortMultiThreading(arr2)
        start = time.time()
        sorter.sort()
        par_time = (time.time() - start) * 1000

        speedup = seq_time / par_time if par_time > 0 else 0

        print(f"{size:<15} {seq_time:.2f} ms {' '*5} {par_time:.2f} ms {' '*5} {speedup:.2f}x")

    print("-" * 60)

if __name__ == '__main__':
    try:
        n = int(input("Enter size of array: "))
        arr = [int(x) for x in input(f"Enter {n} integers: ").split()]
        sorter = QuickSortMultiThreading(arr.copy())
        sorter.sort()
        print("Sorted array:", ' '.join(map(str, sorter.arr)))
        run_performance_test()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

#Output:
# Enter size of array: 10 
# Enter 10 integers: 34 7 23 32 5 62 78 1 45 9
# Sorted array: 1 5 7 9 23 32 34 45 62 78
# Performance Comparison: Sequential vs Parallel Quicksort
# ------------------------------------------------------------
# Array Size      Sequential (ms)      Parallel (ms)        Speedup   
# ------------------------------------------------------------
# 10000           13.11 ms       17.52 ms       0.75x
# 100000          149.23 ms       149.65 ms       1.00x
# 1000000         2083.84 ms       2130.14 ms       0.98x
# ------------------------------------------------------------