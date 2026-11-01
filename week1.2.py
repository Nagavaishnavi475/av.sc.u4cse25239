p = float(input("Enter the Principal Growth Factor:"))
n = int(input("Enter the Number of Years:"))
def power(p, n):
    if n == 0:
        return 1
    else:
        return p * power(p, n - 1)
Output = power(p, n)
print("Growth of an Investment", Output)
