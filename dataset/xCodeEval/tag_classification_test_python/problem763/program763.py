def program763():
    a = input().split(); n=int(a[0]); m=int(a[1]);
    s = n
    while(n):
        s+=n//m
        
        n=n//m + n%m
        
        if n%m==n:
            break
            
    print(s)