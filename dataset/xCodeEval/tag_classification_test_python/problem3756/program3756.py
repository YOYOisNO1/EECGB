def program3756():
    n,m=map(int,input().split(' '))
    k=m-1
    if(m==1 and n==0):
        print("YES")
    else:
        print("YES" if (n - k) % 2 == 0 and n >= k and k >= 0 and m != 1 else "NO")
    
    
    
    
    
    