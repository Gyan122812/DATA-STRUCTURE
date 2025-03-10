def prefixSum():
   
    N = int(input("Enter Number of elements: "))
    arr = []
    
    print(f"Enter {N} elements: ")
    
    for _ in range(N):
        arr.append(int(input()))  
    

    prefix = [0] * N
    prefix[0] = arr[0]
    
    for i in range(1, N):
        prefix[i] = prefix[i - 1] + arr[i]
    

    Q = int(input("Enter number of queries: "))
    
    print(f"Enter {Q} queries (L R):")
    
    for _ in range(Q):

        L = int(input("Enter L: "))
        R = int(input("Enter R: "))
        

        if L == 0:
            sum = prefix[R]
        else:
            sum = prefix[R] - prefix[L - 1]
        
        print(f"Sum from {L} to {R} = {sum}")


prefixSum()
