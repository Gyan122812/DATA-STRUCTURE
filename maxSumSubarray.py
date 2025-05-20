# def max_sum_subarray(arr, k):
#     n = len(arr)
#     if n < k:
#         return -1
    
#     max_sum = curr_sum = sum(arr[:k])
    
#     for i in range(k, n):
#         curr_sum += arr[i] - arr[i-k]
#         max_sum = max(max_sum, curr_sum)
    
#     return max_sum

# # Example
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# print("Maximum sum of subarray of size", k, "is:", max_sum_subarray(arr, k))




