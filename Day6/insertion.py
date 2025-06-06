def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i  - 1

        # Move elements of arr [0..i-1], that are greater than key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

# Example usage
arr = [9, 3, 1, 5, 4]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)