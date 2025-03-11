def SplitArray(arr):
    for i in range( len(arr)):
        sum1 = sum(arr[:i])
        
        for j in range(i+1,  len(arr)):
          sum2 = sum(arr[i: len(arr)])
        
        if sum1 == sum2:
            return True
    
    return False

N = int(input("Enter Number of elements: "))
arr = []

print(f"Enter {N} elements: ")

for _ in range(N):
    arr.append(int(input()))
print(SplitArray(arr))  


#    for i in range(1, len(arr)):
#       sum1 = sum(arr[:i])
      
#      sum2 = sum(arr[i: len(arr)])
    
#    if sum1 == sum2:
#       return True

#    return False

    
