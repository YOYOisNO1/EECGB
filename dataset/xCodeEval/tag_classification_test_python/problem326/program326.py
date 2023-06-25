    import math
def inp():
        return int(input())
def linp():
        return map(int, input().split())
    m, d = linp()
    li = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = 1
    for i in xrange(li[m]):
        if(d==7):
            d = 1
        else:
            if(d==1 and i!=0):
                ans+=1
            d+=1
    print(ans)