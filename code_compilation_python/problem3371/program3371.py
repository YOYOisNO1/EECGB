def program3371():
    n,m = [int(i) for i in input().split()]
    if n%2 == 1:
        if m >= (n-1)/2:
            print (int((n-1)*n/2))
        else:
            t = 0
            for i in range((n-1)/2-m):
                t += 4*i+3
            print (int((n-1)*n/2-t))
    else:
        if m >= n/2:
            print (int((n-1)*n/2))
        else:
            t = 0
            for i in range(n/2-m):
                t += 4*i+1
            print (int((n-1)*n/2-t))
    
            
                