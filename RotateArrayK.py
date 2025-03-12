def rotate_array(arr, k):
    n = len(arr)
    k = k % n  
    return arr[-k:] + arr[:-k]  # arr[-k:] gives the last k elements of the list + arr[:-k] gives everything except the last k elements.

arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array(arr, k)
print(rotated_arr)
