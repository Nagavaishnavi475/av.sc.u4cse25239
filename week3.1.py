n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Bubble Sort algorithm
for i in range(n - 1):
    for j in range(n - i - 1):
        # Change '<' to '>' for ascending order
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Elements after Bubble Sort (Ascending):")
print(arr)
