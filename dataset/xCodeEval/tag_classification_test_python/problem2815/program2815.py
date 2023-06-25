def program2815():
    n, k=map(int,input().split())
    s=str(n)
    l=[]
    for i in range(len(s)):
        l.append(int(s[i]))
    
    a=l.count(0)
    if a>=k:
       count=0
       x=0
       i=len(l)
       while i!=0:
          if count!=k:
             if l[i-1]!=0:
                x+=1
        
             else:
                count+=1 
            
             i-=1    
          else:
             break
    
       print(x)   
    
    else:
       if 0 in l:
          print(len(l)-1)
       else:
          print(len(l))   
             