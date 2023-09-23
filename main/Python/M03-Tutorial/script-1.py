def sort012(arr, N):
    low = 0  # Pointer to the beginning of the array
    high = N - 1  # Pointer to the end of the array
    mid = 0  # Pointer to the current element being considered

    while mid <= high:
        if arr[mid] == 0:
            # If the current element is 0, swap it with the element at the low pointer
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # If the current element is 1, just move the mid pointer forward
            mid += 1
        else:
            # If the current element is 2, swap it with the element at the high pointer
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

arr = [2, 0, 2, 1, 1, 0]
N = len(arr)
sort012(arr, N)
print(arr)  
