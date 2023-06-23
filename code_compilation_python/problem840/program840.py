def lcm(a,b):
        for i in range(b,b*b):
            if(i%a==0 and i%b==0):
                return i
    
    a,b,c,d=map(int,input().split())
    e=lcm(a,b)
    value=0
    for i in range(c,d+1):
        if(i%e==0):
            value+=1
    print(value)