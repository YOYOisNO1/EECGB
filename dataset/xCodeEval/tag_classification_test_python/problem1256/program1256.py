def domino(n,m):
        a=sum(n)
        b=sum(m)
        count=0
        if a%2==0 and b%2==0:
            print(0)
        elif a%2==0 and b%2!=0:
            print(-1)
        elif b%2==0 and a%2!=0:
            print(-1)
        elif a%2!=0 and b%2!=0 and len(n)==1:
            print(-1)
        else:
            for i in range(len(n)):
                if n[i]%2==0 and m[i]%2!=0:
                    count+=1
                elif m[i]%2==0 and n[i]%2!=0:
                    count+=1
                else:
                    continue
            if count>0:
                print(1)
            else:
                print(-1)
    a=input()
    n=[]
    m=[]
    for i in range(int(a)):
        x,y=input().split()
        n.append(int(x))
        m.append(int(y))
    domino(n,m)
        