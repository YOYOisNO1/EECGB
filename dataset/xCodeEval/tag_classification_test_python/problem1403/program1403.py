def program1403():
    k,n,w=input().split()
    k=int(k)
    n=int(n)
    w=int(w)
    sum=0
    for i in range(w+1):
        sum+=k*i
    if n<sum:
        print(int(sum-n))
    else:
        print(0)