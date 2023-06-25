def program6034():
    l,r =map(int,input().split())
    a=bin(r)[2:]
    
    b='0'*(len(a)-len(bin(l)[2:]))+bin(l)[2:]
    ans = 0
    for i in range(len(a)):
        if a[i]!=b[i]:
            ans = 2**(len(a)-i)-1
            break
    print(ans)
        
    