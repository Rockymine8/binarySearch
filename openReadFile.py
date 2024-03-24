def openFile():
    #open file numbers.txt in read mode
    file = open("numbers.txt", "r")

    #save the data from numbers.txt
    data = file.read()

    #convert data to a list
    arr = data.split(' ')

    #convert each element in the list into an int
    arr = [int(x) for x in arr]

    #close the file
    file.close()
    
    return arr