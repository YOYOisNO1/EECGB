def program837():
    a,b,c,d=map(int,input().split()+input().split())
    
    e=0
    
    for i in range(c):
    
     if a>b:a,b=b,a
    
     e+=a
    
     a+=d
    
    print(e)
    
    
    
    # Made By Mostafa_Khaled