def program834():
    nm=input().split()
    n=int(nm[0])
    m=int(nm[1])
    
    int i=int(n/m)
    int j=n%m
    for x in range(m-j):
        print(i,end=" ")
    for x in range(j):
        print(i+1,end=" ")