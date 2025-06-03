def selection_sort(arr):
    
    # check the size of array
    n = len(arr)

    for i in range(n):
        # Assume the current element is the minimum 
        min_index = i 

        # find the smallest element's index in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
