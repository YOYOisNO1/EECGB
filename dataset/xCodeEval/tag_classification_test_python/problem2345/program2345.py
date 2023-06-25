def program2345():
    n = int(input())
    s = map(int,input().split())
    l1 = []
    '''for i in range(n+1):
        for j in range(i):
            l1.append(abs(360 - 2*sum(s[j:i])))
    print(min(l1)''')
    print(min(abs(360-2*sum(s[j:i]))for) i in range(n+1) for j in range(i))