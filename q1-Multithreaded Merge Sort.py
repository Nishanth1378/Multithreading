import threading
import time
import random
from queue import Queue

def merge(left, right):
    """Merge two sorted sublists into one sorted list."""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    """Perform a standard single-threaded merge sort."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def multi_threaded_merge_sort(arr, num_threads):
    """
    Perform a multithreaded merge sort by dividing the array and sorting parts in parallel.
    
    Args:
        arr: List of integers to be sorted.
        num_threads: Number of threads to use.
    
    Returns:
        Sorted list.
    """
    if num_threads <= 1 or len(arr) <= 1:
        return merge_sort(arr)

    size = len(arr) // num_threads
    sublists = [arr[i:i+size] for i in range(0, len(arr), size)]
    sorted_queue = Queue()

    def sort_sublist(sublist):
        sorted_queue.put(merge_sort(sublist))

    threads = []
    for sublist in sublists:
        thread = threading.Thread(target=sort_sublist, args=(sublist,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    sorted_sublists = []
    while not sorted_queue.empty():
        sorted_sublists.append(sorted_queue.get())

    # Merge sorted sublists pairwise until one remains
    while len(sorted_sublists) > 1:
        merged = []
        for i in range(0, len(sorted_sublists), 2):
            if i + 1 < len(sorted_sublists):
                merged.append(merge(sorted_sublists[i], sorted_sublists[i+1]))
            else:
                merged.append(sorted_sublists[i])
        sorted_sublists = merged

    return sorted_sublists[0]

def compare_sorts(arr_size, num_threads):
    """Compare single-threaded and multithreaded merge sort performance."""
    print(f"\n{'-'*20} Array size: {arr_size} {'-'*20}")
    data = [random.randint(1, 1000000) for _ in range(arr_size)]

    start_time = time.time()
    sorted_single = merge_sort(data.copy())
    single_time = time.time() - start_time
    print(f"Single-threaded time: {single_time:.6f} seconds")

    start_time = time.time()
    sorted_multi = multi_threaded_merge_sort(data.copy(), num_threads)
    multi_time = time.time() - start_time
    print(f"Multi-threaded time: {multi_time:.6f} seconds")

    print(f"Results are identical: {sorted_single == sorted_multi}")
    print(f"Speedup: {single_time / multi_time:.2f}x" if multi_time > 0 else "Too fast to measure.")

if __name__ == "__main__":
    input_list = [4, 5, 8, 3, 0, 5, 3, 9, 4, 3]
    num_threads = 2
    print("Original List:", input_list)
    sorted_list = multi_threaded_merge_sort(input_list, num_threads)
    print("Sorted list:", sorted_list)

    print("\n" + "="*50)
    print("\nPerformance comparison:")
    sizes = [10000, 100000, 500000]
    for size in sizes:
        compare_sorts(size, num_threads)
