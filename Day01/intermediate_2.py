import math

def is_prime(n:int) -> bool:
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n < 0:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for _ in range(3, int(math.sqrt(n)) + 1, 2):
        if n % _ == 0:
            return False
    return True


n = int(input("Enter a number: "))
is_prime(n)
print(f"{n} is a prime number" if is_prime(n) else f"{n} is not a prime number")

# We use +1 to include the square root in the range, which might be a factor. Otherwise range() will ignore it