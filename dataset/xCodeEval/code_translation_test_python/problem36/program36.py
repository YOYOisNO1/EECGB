def program36():
    import sys
    
    I = lambda: int(input())
    readline = lambda: sys.stdin.readline().strip('\n')
    RM = readmap  = lambda x=int: map(x,readline().split(' '))
    
    #1321 625 div2
    #C: Remove Adjacent
    n,s = I(),readline()
    for i in range(25,0,-1):
        y = chr(ord('a')+i)
        x = chr(ord('a')+i-1)
        while True: 
            temp = len(s)
            s = s.replace(x+y,x).replace(y+x,x)
            if len(s) == temp:
                break
    print(n-len(s))
    quit()
    #B:Journey Planning
    #overkill approach: dynamic programming; TLE
    #pmax0 = 0
    #bmax = b.copy()
    #for i in range(n-1,-1,-1):
    #    if max0<b[i]:
    #        max0 = max(max0,b[i])
    #        continue
    #    bmax[i] += max([0]+[bmax[j] for j in range(i+1,n) if j-i == b[j]-b[i]])
    #    max0 = max(max0,b[i])
    #print(max(bmax))
    
    #**trick: find common features in the sequence in O(1)**
    d = {}
    for i,x in zip(range(I()),RM()):
        d[x-i] = d.get(x-i,0) + x
    print(max(d.values()))
    quit()
    #A: contest for robots
    n,a,b =I(),[*RM()],[*RM()]
    count1,count2 = 0,0
    for i,j in zip(a,b):
        count1 += i & ~j
        count2 += j & ~i
    print(divmod(count2,count1)[0]+1 if count1 else -1)