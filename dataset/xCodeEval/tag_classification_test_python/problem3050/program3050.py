def gcd(x,y):
        if min(x,y)==0:
            return max(x,y)
        else:
            return gcd(min(x,y),(max(x,y)%min(x,y)))
    a,b=map(int,input().split())
    if abs(a-b)<2:
        print(-1)
    else:
        flag=c=0
        if a%2==1:
            a+=1
        if b%2==1:
            b-=1
        for i in range(a+1,b):
            if gcd(a,i)==1 and gcd(b,i)==1:
                c=i
                flag=1
                break
        if flag==1:
            print(a,c,b)
        else:
            print(-1)