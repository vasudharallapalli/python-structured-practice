def factorial(n: int) -> int:
    result = 1

    for _ in range(2, n + 1):
        result *= _

    print(f"The factorial of {n} is {result}")

def factorial_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = int(input("Enter a number for factorial: "))
result = factorial_recursive(n)
print(f"The factorial of {n} is {result} with recursion.")