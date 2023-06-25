def program3046():
    a,b,c=map(int,input().split())
    d=a
    e=b
    f=c
    a//=3
    b//=2
    c//=2
    m=min(a,b,c)
    a=d-3*m
    b=e-2*m
    c=f-2*m
    if a>3:a=3
    if b>2:b=2
    if c>2:c=2
    nd=m*7
    li=[["011","122","122"],["123","234","235"],["223","345","456"],["223","356","45"]]
    nd+=int(li[a][b][c])
    print(nd)