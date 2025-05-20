# def findEquilibriumIndex(arr):
#     Tsum = sum(arr)
#     Lsum = 0  

#     for i in range(len(arr)):


#         Rsum = Tsum - Lsum - arr[i] # calc right sum by subtracting left sum and current element from total sum
        
#         if Lsum == Rsum:
#             return i  
        
#         Lsum += arr[i]
    
#     return -1  
  

# arr = [2,5,5,2]
# index = findEquilibriumIndex(arr)

# if index != -1:
#     print(f"Equilibrium index is: {index}")
# else:
#     print("No equilibrium index found.")






# def find_equilibrium_index(arr):
#     total_sum = sum(arr)
#     left_sum = 0
    
#     for i in range(len(arr)):
#         if left_sum == (total_sum - left_sum - arr[i]):
#             return i
#         left_sum += arr[i]
#     return -1  # No equilibrium index found

# # Example
# arr = [1, 3, 5, 2, 2]
# print("Equilibrium index is:", find_equilibrium_index(arr))




