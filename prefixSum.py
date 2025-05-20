# def prefixSum():
   
#     N = int(input("Enter Number of elements: "))
#     arr = []
    
#     print(f"Enter {N} elements: ")
    
#     for _ in range(N):
#         arr.append(int(input()))  
    

#     prefix = [0] * N
#     prefix[0] = arr[0]
    
#     for i in range(1, N):
#         prefix[i] = prefix[i - 1] + arr[i]
    

#     Q = int(input("Enter number of queries: "))
    
#     print(f"Enter {Q} queries (L R):")
    
#     for _ in range(Q):

#         L = int(input("Enter L: "))
#         R = int(input("Enter R: "))
        

#         if L == 0:
#             sum = prefix[R]
#         else:
#             sum = prefix[R] - prefix[L - 1]
        
#         print(f"Sum from {L} to {R} = {sum}")


# prefixSum()











def create_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix

def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    else:
        return prefix[R] - prefix[L-1]

# Example usage
arr = [1, 3, 5, 7, 9]
prefix = create_prefix_sum(arr)
L, R = 1, 3  # Sum from index 1 to 3 (3+5+7=15)
print("Sum of elements from index", L, "to", R, "is:", range_sum(prefix, L, R))

