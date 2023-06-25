def program1231():
    n = int(input())
    l = list(map(int, input().split()))
    x=max(l)
    for i in range(1,x+1):
        if x%i==0:
            l.remove(i)
    print(x,max(l))