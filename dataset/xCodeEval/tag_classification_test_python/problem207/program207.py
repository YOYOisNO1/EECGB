    r1=lambda:input()
    r2=lambda:map(int,input().split())
    r3=lambda:list(map(int,input().split()))
    st=str(input())
    h=st[0:2]
    m=st[3:5]
    h=int(h)
    m=int(m)
def pel(a,b):
        a=str(a)
        b=str(b)
        if(len(a)==1):
            a="0"+a
        if(len(b)==1):
            b="0"+b
        if(a[1]==b[0] and b[1]==a[0]):
            return 1
        else:
            return 0
    c=0
    for i in range(0,10000):
        if pel(h,m):
            print(c)
            break
        m=m+1
        c=c+1
        if(m==60):
            h=h+1
            m=00
        if(h==24):
          h=0
        #print(h,m)
    