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

    
# array can be splited or not
def can_be_split(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        left_sum += arr[i]
        
        if left_sum * 2 == total_sum:
            return True
    return False

# Example
arr = [1, 2, 3, 3,1, 2]
print("Can be split into two parts:", can_be_split(arr))
