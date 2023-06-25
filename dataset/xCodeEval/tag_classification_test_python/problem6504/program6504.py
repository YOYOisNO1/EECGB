def program6504():
    A,B=map(int,input().split())
    y,g,b=map(int,input().split())
    count=0
    X=(y*2)+(g*1)
    c1=abs(X-A)
    if A<X:
        count+=c1
    Y=(g*1)+(b*3)
    c2=abs(Y-B)
    if B<Y:
        count+=c2
    
    print(count)