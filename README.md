# 🧵 Multithreaded Algorithms in Python

This repository showcases three Python programs using multithreading and concurrency to improve performance in:

- ✅ Merge Sort  
- ✅ Quick Sort  
- ✅ File Downloading

Each program includes both single-threaded and multithreaded versions to allow side-by-side performance comparisons.

---

## 📂 Project Structure

| File                           | Description                                                        |
|---------------------------------|------------------------------------------------------------------|
| `multithreaded_merge_sort.py`  | Multi-threaded Merge Sort implementation with performance comparison |
| `multithreaded_quick_sort.py`  | Quick Sort using ThreadPoolExecutor and depth control              |
| `multithreaded_file_download.py` | Concurrent vs sequential file downloader using threading in Google Colab |

---

## 🧪 Features

### 🧬 Multithreaded Merge Sort

- Divides an array into sublists  
- Sorts each sublist in parallel using threads  
- Merges sorted sublists sequentially  
- Shows time difference between single-threaded and multi-threaded sorting

### ⚡ Multithreaded Quick Sort

- Uses `ThreadPoolExecutor` with recursion depth control  
- Compares performance with traditional single-threaded quicksort  
- Includes benchmarking for arrays up to 1 million elements

### 🌐 File Downloader with Threading

- Downloads multiple files sequentially or concurrently using `threading.Thread`  
- Accepts URLs via manual input or uploaded `.txt` file  
- Compares download times to show multithreaded speedup  
- Compatible with Google Colab

---

## 🚀 How to Run

### 🔧 Prerequisites

- Python 3.x  
- (Optional) Google Colab for file downloader

---

## 🧪 Example Execution

---

### 1️⃣ Multithreaded Merge Sort

```bash
python merge_sort_threaded.py
Original List: [4, 5, 8, 3, 0, 5, 3, 9, 4, 3]
Sorted list:   [0, 3, 3, 3, 4, 4, 5, 5, 8, 9]

==================================================
Performance comparison:

Array size: 10000
Single-threaded time: 0.042353 sec
Multi-threaded time: 0.025774 sec
Results identical: True
Speedup: 1.64x

Array size: 100000
Single-threaded time: 0.511037 sec
Multi-threaded time: 0.289213 sec
Results identical: True
Speedup: 1.77x

Array size: 500000
Single-threaded time: 2.611278 sec
Multi-threaded time: 1.469852 sec
Results identical: True
Speedup: 1.78x
2️⃣ Multithreaded Quick Sort
Sample Input:

Enter size of array: 10
Enter 10 integers: 34 7 23 32 5 62 32 2 8 1

Sample Output:
Sorted array: 1 2 5 7 8 23 32 32 34 62
| Array Size | Sequential (ms) | Parallel (ms) | Speedup |
| ---------- | --------------- | ------------- | ------- |
| 10,000     | 46.34           | 25.77         | 1.80x   |
| 100,000    | 428.12          | 241.59        | 1.77x   |
| 1,000,000  | 4422.19         | 2365.88       | 1.87x   |



3️⃣ Multithreaded File Downloader


python multithreaded_downloader.py

Sample Input:
Enter 1 to input URLs manually, 2 to load from a text file: 1
How many URLs? 3
Enter URL: https://example.com/file1.jpg
Enter URL: https://example.com/file2.jpg
Enter URL: https://example.com/file3.jpg


Sample Output:

Starting Sequential Download...
Downloaded: file1.jpg
Downloaded: file2.jpg
Downloaded: file3.jpg
Sequential download completed in 12.87 sec

Starting Threaded Download...
Downloaded: file1.jpg
Downloaded: file2.jpg
Downloaded: file3.jpg
Concurrent download completed in 4.38 sec

Summary:
Sequential Time: 12.87 sec
Threaded Time: 4.38 sec
Speedup: 2.94x

Downloading files to your system...







