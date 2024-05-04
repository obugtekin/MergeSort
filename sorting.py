import numpy as np  # Importing NumPy library for array manipulation
import time  # Importing time library for measuring execution time
from multiprocessing import Pool, cpu_count  # Importing multiprocessing module for parallel processing

def merge_sort(arr):
    # Base case: If the array has 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    # Merge two sorted arrays into one sorted array
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def parallel_merge_sort(arr):
    # Determine the number of CPU cores available
    num_cores = cpu_count()
    #print(num_cores)
    # Calculate the chunk size based on the number of cores
    chunk_size = len(arr) // num_cores
    # Divide the array into chunks
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    # Use a Pool of worker processes to perform parallel sorting
    with Pool(num_cores) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)  # Sort each chunk in parallel

    # Merge sorted chunks sequentially
    result = merge(sorted_chunks[0], sorted_chunks[1])
    for i in range(2, num_cores):
        result = merge(result, sorted_chunks[i])

    return result

if __name__ == "__main__":
    # Generate a large array of random integers
    large_array = np.random.randint(0, 10000000, size=400000)

    print("Generated Array:", large_array)

    # Measure sequential sorting time
    start_time = time.time()
    sorted_array_sequential = merge_sort(large_array.copy())
    sequential_time = time.time() - start_time

    # Measure parallel sorting time
    start_time = time.time()
    sorted_array_parallel = parallel_merge_sort(large_array.copy())
    parallel_time = time.time() - start_time

    # Print sorting times
    print("Sequential Sorting Time:", sequential_time)
    print("Parallel Sorting Time:", parallel_time)

    # Calculate time difference and percentage difference
    time_difference = sequential_time - parallel_time
    percentage = (time_difference / sequential_time) * 100

    print("Time difference between sequential and parallel sorting:", time_difference)
    print("Percentage difference between sequential and parallel sorting:%", percentage)
