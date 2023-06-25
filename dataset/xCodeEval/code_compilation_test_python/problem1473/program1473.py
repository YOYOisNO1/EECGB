def program1473():
    x,y=input.split()
    x=int(x)
    y=int(y)
    while(y>0&&x>0):
     if y>x:
        y-=2
        x-=1
        ans+=1
     else  :
         if x==1:
             ans-=1
        x-=2
        y-=1
        ans+=1
    print(ans)    