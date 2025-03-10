def findEquilibriumIndex(arr):
    Tsum = sum(arr)
    Lsum = 0  

    
    for i in range(len(arr)):

# Calculate the right sum by subtracting the left_sum and the current element from the total sum
        Rsum = Tsum - Lsum - arr[i]
        
        if Lsum == Rsum:
            return i  
        
        Lsum += arr[i]
    
    return -1  
  

arr = [4, 2, 3, 1, 5]
index = findEquilibriumIndex(arr)

if index != -1:
    print(f"Equilibrium index is: {index}")
else:
    print("No equilibrium index found.")