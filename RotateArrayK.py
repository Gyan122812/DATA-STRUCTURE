def rotate_array(arr, k):
    n = len(arr)
    k = k % n  
    return arr[-k:] + arr[:-k]  # arr[-k:] gives the last k elements of the list + arr[:-k] gives everything except the last k elements.

arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array(arr, k)
print(rotated_arr)



# def rotate_array(arr, k):
#     n = len(arr)
#     k = k % n  
#     result = []

#     for i in range(n - k, n):
#         result.append(arr[i])

#     for i in range(n - k):
#         result.append(arr[i])

#     return result

# arr = [1, 2, 3, 4, 5]
# k = 2
# rotated_arr = rotate_array(arr, k)
# print(rotated_arr)

