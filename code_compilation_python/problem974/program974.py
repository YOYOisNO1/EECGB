def program974():
    from bisect import *
    from sys import *
    input = stdin.readline
    
    A,B,C,D = map(int,input().split())
    
    n = max(D+2,B+C+2)
    a = [0]*(n)
    
    for i in range(A,B+1):
        l = i + B
        r = i + C + 1
        a[l] += 1
        a[r] -= 1
        
        
    sn = 0 
    for i in range(n):
        sn += a[i]
        a[i] = sn
    
    sn = 0 
    for i in range(n-1,-1,-1):
        sn += a[i]
        a[i] = sn
     
        
    sn = 0 
    for i in range(C,D+1):
        sn += a[i+1]
    
    stdout.write(str(sn)+'\n')from bisect import *
    from sys import *
    input = stdin.readline
    
    A,B,C,D = map(int,input().split())
    
    n = max(D+2,B+C+2)
    a = [0]*(n)
    
    for i in range(A,B+1):
        l = i + B
        r = i + C + 1
        a[l] += 1
        a[r] -= 1
        
        
    sn = 0 
    for i in range(n):
        sn += a[i]
        a[i] = sn
    
    sn = 0 
    for i in range(n-1,-1,-1):
        sn += a[i]
        a[i] = sn
     
        
    sn = 0 
    for i in range(C,D+1):
        sn += a[i+1]
    
    stdout.write(str(sn)+'\n')from bisect import *
    from sys import *
    input = stdin.readline
    
    A,B,C,D = map(int,input().split())
    
    n = max(D+2,B+C+2)
    a = [0]*(n)
    
    for i in range(A,B+1):
        l = i + B
        r = i + C + 1
        a[l] += 1
        a[r] -= 1
        
        
    sn = 0 
    for i in range(n):
        sn += a[i]
        a[i] = sn
    
    sn = 0 
    for i in range(n-1,-1,-1):
        sn += a[i]
        a[i] = sn
     
        
    sn = 0 
    for i in range(C,D+1):
        sn += a[i+1]
    
    stdout.write(str(sn)+'\n')