def countdown(n):
    if n <= 0:
        print("Rocket Launched")
    else:
        print(n)
        countdown(n - 1)
n = int(input("Enter the number: "))
countdown(n)
