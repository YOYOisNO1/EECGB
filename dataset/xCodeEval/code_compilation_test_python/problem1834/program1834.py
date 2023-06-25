def solve():
        li =  {"0":6, "1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6}
        res = 0
        a, b = map(int, input().split())
        b += 1
        for i in range(a, b):
            s  = str(i)
            for e in s:
                res += li[e]
        print(res)
    
     solve()