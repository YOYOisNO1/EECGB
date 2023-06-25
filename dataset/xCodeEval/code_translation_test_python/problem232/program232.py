def program232():
    arr1 = input().split(" ")
    arr2 = input().split(" ")
    n = int(input())
    for i in range(len(arr1)):
        arr1[i] = int(arr1[i])
        arr2[i] = int(arr2[i])
    
    if sum(arr1)!= 0:
        n -= (sum(arr1)-1)/5+1
    if sum(arr2)!= 0:
        n -= (sum(arr2)-1)/10+1
    if n >= 0:
        print("YES")
    else:
        print("NO")
    