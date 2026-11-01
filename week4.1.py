def quicksort(a,low,high):
    if low < high:
        i = low
        j = high
        pivot = low
        while i < j:
            while i < len(a) and a[i]<=a[pivot]:
                i +=1
            while a[j] > a[pivot]:
                j = j -1
            if i < j:
                a[i],a[j] = a[j],a[i]
        a[j],a[pivot] = a[pivot],a[j]
        quicksort(a,low,j-1)
        quicksort(a,j+1,high)
a = list(map(int,input("Enter numbers to sort:").split(" ")))
n = len(a)
quicksort(a,0,n-1)
print("Sorted array:")
print(a)
