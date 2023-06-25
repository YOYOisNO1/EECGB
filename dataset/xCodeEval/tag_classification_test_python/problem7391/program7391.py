    from sys import stdin, stdout
    from collections import Counter, defaultdict
    from itertools import permutations, combinations
    input = stdin.readline
    pr = stdout.write
    
    
def in_arr():
        return map(int,input().split())
    
    
def pr_num(n):
        stdout.write(str(n)+'\n')
    
    
def pr_arr(arr):
        pr(' '.join(map(str,arr))+'\n')
    
    
    range = xrange # not for python 3.0+
    
    # main code
    
    n,m=in_arr()
    deg=[0]*n
    x,y,z=0,0,0
    ans=['a']*n
    adj=defaultdict(Counter)
    for i in range(m):
        u,v=in_arr()
        deg[u-1]+=1
        deg[v-1]+=1
        adj[u-1][v-1]=1
        adj[v-1][u-1]=1
    for i in range(n):
        if deg[i]==n-1:
            y+=1
            ans[i]='b'
    for i in range(n):
        if ans[i]=='a':
            ans[i]='c'
            for j in range(n):
                if adj[i][j] and ans[j]!='b':
                    
                    ans[j]='c'
            break
    f=0
    for i in range(n):
        for j in range(i+1,n):
            if (adj[i][j]^int(abs(ord(ans[j])-ord(ans[i]))<=1)):
                f=1
                break
        if f:
            break
    if f:
        pr('No')
    else:
        pr('Yes\n')
        pr(''.join(ans))