def sum_of_digits(n):
    M = 0
    while n > 0:
        M += n % 10 
        n = n // 10  
    return M

number = 12345  
SD = sum_of_digits(number)
print("Sum of digits",number,"is : ", SD)
