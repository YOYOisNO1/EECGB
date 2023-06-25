def program351():
    n,m=map(int,input().split())
    li=list(map(int,input().split()))
    li=sorted(li)
    li1=sorted(list(map(int,input().split())))
    for i in li1:
     if i in li:
      a=i
    a1=min(li)
    b1=min(li1)
    b=min((a1*10+b1),(b1*10+a1))
    print(min(a, b))
    