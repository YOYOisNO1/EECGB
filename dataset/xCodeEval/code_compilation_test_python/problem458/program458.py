def program458():
    n = input().split()
    a = int(n[0])
    b = int(n[1])
    c = []
    t = input().split()
    for i in range(a):
        c.append([int(t[i]),0,i])
        c[i][1] = c[i][0] // b
    c.sort(key = lambda x:(x[1],x[2])
    print(c[0][2]+1)