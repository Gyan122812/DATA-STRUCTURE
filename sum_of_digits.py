def sum_of_digits(n):
    M = 0
    while n > 0
        M += n % 10 
        n = n // 10  
    return M

num = 12345  
SD = sum_of_digits(num)
print("Sum of digits",num,"is : ", SD)
