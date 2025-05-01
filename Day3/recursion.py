# def func():
#     func()

# func()


#  maximum recursion depth exceeded
#  infinite loop


def printsum (arr, sI):
    #  base condition
    if ( sI >= len(arr)):
        return
    # logic
    print(arr[sI])
    #Recursion call

    printsum(arr, sI+1)
printsum([2,3,5],0)

