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
