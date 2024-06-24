def SelectionSort(arr):
    for i in range(len(arr)):  # Traverse through the list
        min_index = i  # Set the minimum index to the current index
        for j in range(i + 1, len(arr)):  # Traverse through the unsorted part of the list
            if arr[min_index] > arr[j]:  # Check if the current minimum is greater than the element at index j
                min_index = j  # Update the minimum index if a smaller element is found
        # Swap the element at the minimum index with the element at the current index
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr  # Return the sorted list

print(SelectionSort([0,0,23,2342,5,7,9,2]))