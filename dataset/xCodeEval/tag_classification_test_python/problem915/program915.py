def program915():
    from sys import stdin
    N = int(input())
    i = 0
    a = []
    sum = 0
    a = map(int, stdin.readline().split(' '))
    while i < N:
        sum += a[i]
        i+=1
    sum = sum/(N/2)
    j = 0
    i = 0
    while j < N/2:
        while i < N:
            if a[i] > 0:
                break
            i+=1
        k = i+1
        while k < N and (a[k] < 0 or a[k]+a[i] != sum):
            k+=1 
        print(i+1,) k+1
        if k < N:
    	a[k] = -1
        j+=1
        i+=1 