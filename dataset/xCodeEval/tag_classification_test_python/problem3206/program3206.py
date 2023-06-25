def program3206():
    n=int(input())
    l=str(input()).split(" ")
    for i in range(n):
        l[i]=int(l[i])
    l.sort()
    s=0
    for i in range(n//2):
        s+=l[2*i+1]-l[2*i]
    print(s)