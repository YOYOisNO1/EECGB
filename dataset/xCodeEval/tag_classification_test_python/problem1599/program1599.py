def program1599():
    m,n = list(map(int,input().split()))
    l = []
    count = 0
    for i in range(1,m+1):
        if n%i==0:
            l.append(i)
    
    for i in l:
        for j in l:
            if(i*j==n):
                count += 1
    print(count)
    