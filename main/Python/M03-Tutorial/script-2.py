def binarysearch(arr, N, K):
    left, right = 0, N - 1  

    while left <= right:
        mid = left + (right - left) // 2  

        if arr[mid] == K:
            return mid  
        elif arr[mid] < K:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1
\
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = len(arr)
K = 5
result = binarysearch(arr, N, K)
print(result) 