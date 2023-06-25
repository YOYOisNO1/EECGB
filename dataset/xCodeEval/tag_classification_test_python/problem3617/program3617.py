def program3617():
    import sys
    n, t = map(int, input().split())
    s = input()
    a = []
    for i in range(n):
        a.append(s[i])
    for k in range(t):
        j = 0
        for i in range(n-1):
            if j==1:
                j=0
                #print(j,) i, a[i], a[i+1] 
                continue
            elif a[i]=='B' and a[i+1]=='G' and j==0:
                a[i]='G'
                a[i+1]='B'
                j = 1
               # print(j,) i, a[i], a[i+1]
            else:
                #print(j,) i, a[i], a[i+1]
                continue
    for i in range(n):
        sys.stdout.write(a[i])