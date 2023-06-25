def program3724():
    x=input()
    x=x.split(' ')
    n=int(x[0])
    d=int(x[1])
    x=input()
    x=x.split(' ')
    for i in range(n):
        x[i]=int(x[i])
    x.sort()
    l = []
    for i in range(0, n):
        for j in range(i+1, n):
            if (x[j]-x[i])<=d:
                l.append(i + (n - j) - 1)
    if l == []:
        print(n-1)
    else:
         print(min(l))