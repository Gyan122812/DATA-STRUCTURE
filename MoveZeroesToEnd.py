def moveZeroes(nums):
    n = len(nums)
    if n <= 0:
        return  
    
    temp = [0] * n  
    j = 0
    
    for i in range(n):
        if nums[i] != 0:
            temp[j] = nums[i]
            j += 1
    
    for i in range(n):
        nums[i] = temp[i]


nums = [0, 1, 0, 3, 12]
print("Before moveZeroes:", nums)
moveZeroes(nums)
print("After moveZeroes:", nums) 



# def moveZeroes(nums):
#     n = len(nums)
#     if n <= 0:
#         return  
    
#     temp = [0] * n  
#     j = n-1
    
#     for i in range(n - 1, -1, -1):
#         if nums[i] != 0:
#             temp[j] = nums[i]
#             j -= 1
    
#     for i in range(n):
#         nums[i] = temp[i]


# nums = [1,0,1,0,0,1,0]
# print("Before moveZeroes:", nums)
# moveZeroes(nums)
# print("After moveZeroes:", nums)

