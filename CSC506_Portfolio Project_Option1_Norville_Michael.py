"""
@author: Michael Norville
CSC506 - Portfolio Project - Option 1

Using a random number generator, create a list of 500 integers. 
Perform a benchmark analysis using sorting algorithms. Plot results 
What is the difference in speed between the different sorting algorithms? 
"""
#import functions
import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

#Create list of 500 random ints
rand_ints = random.sample(range(3000,46000), 500)
runtimes = 1000 #number of times each sorting algorithm is ran

#Define sorting algorithm - Selection Sort
def selection_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

#Define sorting algorithm - Inserstion Sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

#Define sorting algorithm - Quick Sort
def quick_sort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[random.randint(0, len(array) - 1)]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quick_sort(low) + same + quick_sort(high)

#Define sorting algorithm - Merge Sort
def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

#Create list of sorting algorithms
sorting_algorithms = {
    'Selection Sort': selection_sort,
    'Insertion Sort': insertion_sort,
    'Quick Sort': quick_sort,
    'Merge Sort': merge_sort}

sortedList = quick_sort(rand_ints) 
#Run, time, print list of sorting algorithms
for algorithm, sortIt in sorting_algorithms.items():
    times = timeit.repeat(lambda: sortIt(rand_ints.copy()), number=1, 
                          repeat = runtimes)
    plt.plot(times, label=algorithm)
    print(algorithm, 'took on average', np.mean(times), 'seconds to run a', 
          len(rand_ints), 'long list of random integers', runtimes, 'times.')

#Format performance plot
plt.title('Performance of Sorting Algorithms')
plt.xlabel('Run Number')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()