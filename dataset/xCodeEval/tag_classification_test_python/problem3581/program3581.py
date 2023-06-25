def program3581():
    n,t = input().split()
    a = input()
    t = int(t)
    n = int(n)
    arr = [None]*len(a)
    for i in range(len(a)):
        arr[i] = a[i]
    
    for i in range(t):
        j = 0
        while j < n-1:
            if arr[j] == 'B' and arr[j+1] == 'G':
                arr[j] , arr[j+1] = arr[j+1] ,arr[j]
                j += 1
            j += 1
    print("".join(arr))