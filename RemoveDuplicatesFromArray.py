# def remove_duplicates(arr):
#     return list(set(arr))

# arr = [1, 2, 2, 3, 4, 4, 5]
# print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5]



def remove_duplicates(arr):
    result = []
    for i in arr:  
        if i not in result:
            result.append(i)
    return result

arr = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(arr))
