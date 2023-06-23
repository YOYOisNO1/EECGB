def program2340():
    n = int(input())    
    a = list(map(int,input().split()))
    n = a[0]
    k = a[1]
       if 3 * n > k:
           print(3 * n - k)
       else:
            print(0)