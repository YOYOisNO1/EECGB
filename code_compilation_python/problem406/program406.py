def program406():
    n,d=map(int,input().split())
    l= list(map(int,input().split()))
    d=d-sum(l)
    if(n==1 and d==1 and sum(l)==1):
         print("0")
    elif(n-1<=int(d/10) and d>0):
         f=d%10
         if(f>4):
              f=1+int((d/10))*2
         else:
              f=int((d/10))*2
         print(f)
    else:
         print("-1")
    
         
    
              
    
     