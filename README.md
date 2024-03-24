# Search Algorithms

This repository contains Python implementations of different searching and sorting algorithms, which I read about in "Algorithms" by Panos Lauridas.

## Function: binarySearch

This Python code demonstrates a binary search algorithm to search through list of numbers.

```python
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = high + (low - high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid -1
        else:
            return mid
    return -1
```

This function takes in two parameters:

-   'arr': The list of elements, which must be sorted in ascending order.
-   'x': The element to search for in the list.

It returns the index of the element x if found in the list arr, otherwise returns -1.

### Execution Steps

1. Get the list of data by calling the openReadFile module.
2. Prompt the user to input the element to search for.
3. Perform binary search on the sorted list.
4. Print the result whether the element is found or not.

Please ensure that the file 'numbers.txt' contains a list of integers separated by spaces and is sorted in ascending order for accurate results.

### Time and Space Complexity Analysis

**Time Complexity:** _O(log n)_\
The time complexity of the program is O(log n), where n is the number of elements in the input array. This is because the program uses binary search on the array, which has a time complexity of O(log n).

**Space Complexity:** _O(n)_\
The space complexity of the program is O(n), where n is the number of elements in the input array. This is because the program stores the input data in a list, which requires space which is proportional to the number of elements in the input array.

## Function: selectionSort

This Python code demonstrates a selection sort algorithm to sort a list of numbers.

```python

def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        minIndex = i

        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j;

        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp

```

This function takes in one parameter:

-   'arr': The list of elements, an unsorted list of numbers

### Execution Steps

1. Get the list of data by calling the openReadFile module.
2. Perform selection sort on the list.
3. Print the list, ordered in ascending order

### Time and Space Complexity Analysis

**Time Complexity:** _O(n^2)_\
The time complexity of the program is O(n^2), where n is the number of elements in the input array. This is because the program uses a selection sort on the array, which has a time complexity of O(n^2).

**Space Complexity:** _O(1)_\
The space complexity of the program is O(1). This is because the program is an "in-place" algorithm, where the elements are swapped within the original list. This requires a constant amount of space in memory.

## Module: openReadFile

This module is responsible for reading a list of numbers from a file named 'numbers.txt', and converting each item into an integer. The

```python
def openFile():

    file = open("numbers.txt", "r")

    data = file.read()

    arr = data.split(' ')

    arr = [int(x) for x in arr]

    file.close()

    return arr
```

### Execution Steps

1. Open the file numbers.txt in read mode.
2. Read the data from numbers.txt.
3. Convert the data into a list.
4. Convert each element in the list into an integer.
5. Close the file.
6. Return the converted list.

Please ensure that the file 'numbers.txt' contains a list of integers separated by spaces, and is ordered in a way that is needed by the algorithm.
