import openReadFile

#define selectionSort function
def selectionSort(arr):
    #n is the length of the list passed in
    n = len(arr)
    
    #i = current position of the sorted part of the array
    for i in range(n):
        minIndex = i
        
        #for all the unsorted elements
        #j = the index of the element we're currently comparing to i
        for j in range(i + 1, n):
            #if the element of the unsorted array < minimum in sorted
            if arr[j] < arr[minIndex]:
                minIndex = j;
        
        #Swap the found minimum element with the first element
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
            
#call openFile to get list of numbers from the data in numbers.txt
arr = openReadFile.openFile()

selectionSort(arr)

#print the sorted array
print(arr)