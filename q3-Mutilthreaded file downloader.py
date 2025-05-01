import requests
import threading
import time
import os
from google.colab import files
import glob

DOWNLOAD_FOLDER = "/content/downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_file(url, index):
    """Download a single file from the URL."""
    try:
        response = requests.get(url, timeout=10)
        filename = url.split("/")[-1] or f"file_{index}.bin"
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")

def sequential_download(urls):
    """Download all files one by one (sequentially)."""
    for idx, url in enumerate(urls):
        download_file(url, idx)

def threaded_download(urls):
    """Download all files concurrently using threads."""
    threads = []
    for idx, url in enumerate(urls):
        thread = threading.Thread(target=download_file, args=(url, idx))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def get_urls():
    """Prompt user to input or upload URLs."""
    choice = input("Enter 1 to input URLs manually, 2 to load from a text file uploaded here: ")
    urls = []
    if choice == "1":
        n = int(input("How many URLs? "))
        for _ in range(n):
            urls.append(input("Enter URL: ").strip())
    elif choice == "2":
        uploaded = files.upload()
        filename = list(uploaded.keys())[0]
        try:
            with open(filename, 'r') as file:
                urls = [line.strip() for line in file if line.strip()]
        except Exception as e:
            print(f"Error reading file: {e}")
    else:
        print("Invalid choice.")
    return urls

def main():
    """Main function to handle both download modes and performance comparison."""
    urls = get_urls()
    if not urls:
        print("No URLs provided.")
        return

    print("\nStarting Sequential Download...")
    start = time.time()
    sequential_download(urls)
    seq_time = time.time() - start
    print(f"Sequential download completed in {seq_time:.2f} seconds.\n")

    print("Starting Threaded Download...")
    start = time.time()
    threaded_download(urls)
    thread_time = time.time() - start
    print(f"Concurrent download completed in {thread_time:.2f} seconds.\n")

    print("Summary:")
    print(f"Sequential Time: {seq_time:.2f} sec")
    print(f"Threaded Time:  {thread_time:.2f} sec")
    if thread_time > 0:
        print(f"Speedup: {seq_time / thread_time:.2f}x")

    print("\nDownloading files to your system...")
    for file_path in glob.glob(f"{DOWNLOAD_FOLDER}/*"):
        files.download(file_path)

if __name__ == "__main__":
    main()
