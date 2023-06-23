def program2055():
    a,b = input().split()
    c = list(map(int,input().split()))
    a = int(a)
    b = int(b)
    
    a = a*8
    r=0
    cnt =0
    for i in range(len(c)):
        if c[i] %2 ==1:
            c[i] = c[i]+1
            cnt = cnt +1
        r = r+c[i]
        
           
       
    if r > a or r==a and b == a/2 and cnt <n:
        print("NO")
    else:
        print("YES")
            
            
        
        
        