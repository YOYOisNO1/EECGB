def program124():
    #!usr/bin/python
    n = int(input())
    s = 0
    for i in range(n):
        a = int(input())
        s = s+a
    ans = 0
    for i in range(5):
        if not ((s+i)%(n+1)==0):
            ans = ans+1
    print(ans)