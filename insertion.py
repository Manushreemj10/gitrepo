def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[3,9,8,6,5,7]
print("given elements")
print(arr)
insertion_sort(arr)
print("sorted list")
print(arr)
