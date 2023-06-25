def program3232():
    # tutorial codeforces :(
    # مخم گوزید ناموسا
    n, l = map(int, input().split())
    c = list(map(int, input().split()))
    res = 0
    for i in range(1, n):
        c[i] = min(c[i - 1]*2, c[i])
    p = 1 << (n - 1) # 2 ** (n - 1)
    y = l // p
    l-= y * p
    res+= c[n - 1] * y # y or equal to 0 or y > 0
    RES = []
    if l > 0: # if l not equal to 0 then we can take one more (2 ** (n-1)) and recieve to answer
        RES.append(res + c[n - 1])
    
    
    for i in range(n - 2, -1, -1):
       p//= 2
       y = l // p
       if y == 1:
           res+= c[i]
           l-= (1 << i)
           if l > 0:
               RES.append(res + c[i])
       else: # y == 0
           if l > 0:
               RES.append(res + c[i])
    RES.append(res)
    print(min(RES))
    
    
        
    
    
    
    