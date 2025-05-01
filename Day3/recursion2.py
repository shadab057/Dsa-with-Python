def printRev(arr, sI):
    #base conditin
    if(sI >= len(arr)):
        return 
    #Recursion call
    printRev(arr, sI+1)
    #logic
    print(arr[sI])

printRev([4,3,9],0)