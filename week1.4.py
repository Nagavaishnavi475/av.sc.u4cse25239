n = int(input("Enter the Number:"))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(f"Possible ways to arrange {n} different parcels is", factorial(n))
