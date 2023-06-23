def program1935():
    a,b,c = map(int,input().split())
    j = 1
    l = 0
    if b % 2 != 0: 
        for i in range(1,c+1):
            l += i * a
        if l >= b:
            print(l - b)
        else:
            print(0)
    else:
        for u in range(1,c+1):
            j += u * a
        if j >= b:
        print(j - b)
        else:
            print(0)