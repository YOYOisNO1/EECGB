def program6920():
    import sys
    from sys import stdin, stdout
    from collections import deque
    rem=10**9+7
    sys.setrecursionlimit(10 ** 6)
    take = lambda: map(int, stdin.readline().split())
    
    import sys
    from sys import stdin, stdout
    from collections import deque
    rem=10**9+7
    sys.setrecursionlimit(10 ** 6)
    take = lambda: map(int, stdin.readline().split())
    
    a=list(input())
    a.reverse()
    n=0
    ans=0
    if a[0]=='1':
    	ans=1
    for i in range(1,len(a)):
    	ans=(ans*2)%rem
    	n+=1
    	if a[i]=='1':
    		ans=(ans+pow(2,2*n,rem))%rem
    print(ans)
    