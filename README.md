# Binary Search Algorithm

This Python code demonstrates a binary search algorithm to find an element in a sorted list.

## Function: binarySearch

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

## Execution Steps

1. Open the file numbers.txt in read mode.
2. Read the data from numbers.txt.
3. Convert the data into a list.
4. Convert each element in the list into an integer.
5. Close the file.
6. Sort the list in ascending order.
7. Prompt the user to input the element to search for.
8. Perform binary search on the sorted list.
9. Print the result whether the element is found or not.

Please ensure that the file 'numbers.txt' contains a list of integers separated by spaces and is sorted in ascending order for accurate results.
