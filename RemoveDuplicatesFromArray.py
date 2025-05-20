def remove_duplicates(arr):
    return set(arr)

arr = [5, 2, 3, 1, 3, 5, 4, 5]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5]



# def remove_duplicates(arr):
#     R = []
#     for i in arr:  
#         if i not in R:
#             R.append(i)
#     return R

# arr = [1, 1, 2, 2, 3, 3, 4, 4, 5]
# print(remove_duplicates(arr))
