def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range (i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
n=int(input("Enter the number of elements: "))
arr=[]
print("Enter the elements:")
for i in range(n):
    element=int(input())
    arr.append(element)
result=selection_sort(arr)
print("Elements after Selection Sort:")
print(result)
