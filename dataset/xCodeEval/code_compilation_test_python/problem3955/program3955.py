    from itertools import *
    
    n = int(input())
    a = [map(int, input().split()) for _ in xrange(n)]
    
def check(s):
        for u,v,w in a:
            u = str(u)
            x, y = len( set(s)&set(u) ), 0
            for i in xrange(4):
                if s[i]==u[i]:
                    y += 1
            if x-y!=w or y!=v:
                return 0
        return 1
    
    ans, cnt = "", 0
    for s in permutations("0123456789", 4):
        if check("".join(s)):
            ans = "".join(s)
            cnt += 1
    if cnt == 1:
        print ans
    elif cnt == 0:
        print "Incorrect data"
    else:
        print "Need more data"