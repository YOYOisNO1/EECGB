    import sys
    from collections import Counter,defaultdict,deque
    mod = 10**9+7
    INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
    
def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
    
        divisors.sort()
        return divisors
    a,b = inpl()
    st = []
    for z in [a,b]:
        tmp = make_divisors(z)
        for i in range(len(tmp)//2+1):
            s = tmp[i]; t = z//s
            st.append([s,t])
    ttt = make_divisors(a+b)
    for i in range(len(ttt)//2+1)[::-1]:
        y = ttt[i]
        x = (a+b)//y
        # print(x,y)
        for s,t in st:
            if x >= t and y >= s:
                print(2*(x+y))
                quit()