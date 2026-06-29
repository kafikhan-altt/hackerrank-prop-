
n = int(input())
arr = list(map(int, input().split()))

i: int = 0  # type hint, does not enforce type

if(2<=n<=10 and -100<=arr[i]<=100):
    
    arr1=list(set(arr))  #deleting dupli n storing in list instead of set
     
    y=len(arr1)           #new len of arr
    
    for i in range(y):  #bubble sort
        for j in range(y-1-i):
            if arr1[j] > arr1[j+1]:
                temp=arr1[j]
                arr1[j]=arr1[j+1]
                arr1[j+1]=temp
t=len(arr1)
print(arr1[-2])
