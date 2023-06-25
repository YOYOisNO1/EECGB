def program4336():
    #!/usr/bin/python
    inp=input().split()
    a=int(inp[0])
    b=int(inp[1])
    x1=int(inp[2])
    y1=int(inp[3])
    x2=int(inp[4])
    y2=int(inp[5])
    
    x=(x1-y1)/(2*a)-(x2-y2)/(2*a)
    y=(x1+y1)/(2*b)-(x2+y2)/(2*b)
    x=abs(x)
    y=abs(y)
    print min(x,y)+abs(x-y)