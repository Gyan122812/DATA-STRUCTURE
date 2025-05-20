def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


N = int(input("Enter a number to find its factorial: "))
result = factorial(N)
print(f"The factorial of {N} is {result}")
