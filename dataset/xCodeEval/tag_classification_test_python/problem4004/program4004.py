    w,x=map(int,input().split())
    lst=[]
    for i in range(0,30):
        if  pow(w,i)<x*2:
            lst.append(pow(w,i))
    
    n=len(lst)
    lst.sort(reverse=True)
    ans=100000
def rec(a,x,i):
        #print(a)
        global ans
        if a==x:
            ans=1
            return 1
    
        if i==n:
        #ans=-1
            return
        rec(a,x,i+1)
        
        rec(a-lst[i],x,i+1)
        rec(a+lst[i],x,i+1)
        
        
       # print(a)
    
    if w==2 or w==3:
        print(("YES"))
    else:
    
    
        rec(0,x,0)
    
        if ans==100000 :
          print(("NO"))
        else:
          print(("YES"))