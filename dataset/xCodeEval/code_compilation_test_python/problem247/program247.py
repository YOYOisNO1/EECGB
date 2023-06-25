def checker(n):
        d = {4:0,7:0}
        c = 0
        while n:
            r = n%10
            if r in d:
                d[r]+=1
            c+=1
            n//=10
        if d[4]+d[7] == c and d[4]==d[7]:
            return True
        return False
    
    n = int(input())
    c = 0
    while True:
        if checker(n):
            print(n)
            break
        n+=1