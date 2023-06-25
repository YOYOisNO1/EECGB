def program6136():
    # Made By Mostafa_Khaled 
    bot = True 
    a,b,c,d=map(int,input().split())
    
    e=abs(a-c)
    
    f=abs(b-d)
    
    t=0
    
    if (e-f)%2==0:t=2
    
    if e==f:t=1
    
    print((a!=c)+(b!=d),t,max(e,f))
    
    
    # Made By Mostafa_Khaled