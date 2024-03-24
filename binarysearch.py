import openReadFile

#define binarySearch function
#pass in list of elements, and which element to search for
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    
    #while in between the two bounds
    while low <= high: 
        
        #calculate the middle of the two bounds
        mid = high + (low - high) // 2
        
        #if the middle of the array is less x, ignore the left side
        if arr[mid] < x:
            low = mid + 1
        
        #if the middle of the array is greater than x, ignore the right side
        elif arr[mid] > x:
            high = mid -1
            
        #if the middle of the array is x, return x
        else: 
            return mid
        
    #return if element is not in the array
    return -1   


arr = openReadFile.openFile()

#ask what to search for
x = int(input("Input element: "))

#save the result of the binary search
result = binarySearch(arr, x)

#if the element is in the list, print where
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in list")
    

