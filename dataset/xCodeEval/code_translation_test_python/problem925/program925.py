def program925():
    n=int(input())
    k=1
    for i in range(1,n):
        k=k*i
    k=k*2
    k=k/n
    print(int(k))