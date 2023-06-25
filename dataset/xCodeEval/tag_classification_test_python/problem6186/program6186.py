def program6186():
    x1,y1,x2,y2=map(int,input().split())
    ans=[1] if (x1==x2)or(y1==y2) else [2]
    if (x1+y1-x2-y2)%2==1:ans+=[0]
    else :ans+=[1] if ((x1+y1)==(x2+y2))or((x1-y1)==(x2-y2)) else [2]
    ans+=[max(abs(x1-x2),abs(y1-y2))]
    print(' ').join(map(str,ans))