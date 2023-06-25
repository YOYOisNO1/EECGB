    from sys import maxsize, stdout, stdin,stderr
    mod = int(1e9 + 7)
    import re #can use multiple splits
def tup():return map(int,stdin.readline().split())
def I(): return int(stdin.readline())
def lint(): return [int(x) for x in stdin.readline().split()]
def S(): return input().strip()
def grid(r, c): return [lint() for i in range(r)]
def debug(*args, c=6): print('\033[3{}m'.format(c), *args, '\033[0m', file=stderr)
    from  math import  log2,sqrt
    from collections import defaultdict
    # s= S().split()
    # n = I()
    #
    # d='^>v<'
    # if n%2==0:print('undefined')
    # else:
    #     st =d.find(s[0]).__index__()
    #     en = d[(st+n)%4]
    #     if en==s[1]:print('cw')
    #     elif d[(st-n)%4]==s[1]:print('ccw')
    #     else:print('undefined')
    #
    # #when k it is even it will end up in the same position so direction can't be determined
    # #
    # k = I()
    # n =S()
    # arr = sorted(list(map(int,n)))
    # cnt =sum(arr)
    # ans = 0
    # #print(arr,cnt)
    # for i in arr:
    #     if  cnt < k:
    #         cnt+=9 - i
    #         ans+=1
    # print(ans)
    # #increasing sum by 9-d
    from collections import deque
    n,k = tup()
    s =S()
    c = k ; i =0; d = set()
    di = defaultdict(int)
    for i in s:
        di[i]+=1
    c =k;gates = set()
    d= deque()
    i =0; f = 1
    while i < n:
        if s[i] in gates:
            pass
        else:
            gates.add(s[i])
            if len(gates) >k:
                f =0
                break
        di[s[i]]-=1
        if di[s[i]]==0:
            gates.discard(s[i])
        i+=1
    #op
    if f==0:print("YES")
    else:print("NO")
    
    
    
    
    