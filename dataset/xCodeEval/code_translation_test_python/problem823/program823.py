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
        for i in arr:
            stdout.write(str(i)+' ')
        stdout.write('\n')
    
    
    range = xrange # not for python 3.0+
    
    
    # main code
    
def check(n,m,l,mid):
        temp=0
        c=0
        k=mid
        for i in range(0,n,k):
            for j in range(i,min(n,i+k)):
                #print(mid,i,j,l[j]-c)
                temp+=max(0,l[j]-c)
            c+=1
        #print(temp,m)
        if temp>=m:
            return 1
        return 0
    n,m=in_arr()
    l=in_arr()
    if sum(l)<m:
        print(-1)
        exit()
    l.sort(reverse=True)
    l1=1
    r1=n
    ans=n
    while l1<=r1:
        mid=(l1+r1)/2
        if check(n,m,l,mid):
            ans=mid
            r1=mid-1
        else:
            l1=mid+1
    pr_num(ans)