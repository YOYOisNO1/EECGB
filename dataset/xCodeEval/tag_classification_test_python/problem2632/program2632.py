def crum(x):
        y=''
        for i in range(x):
            y+='|'
        return y
    
    a,b = input().split('+')
    
    s=a+"+"+b
    
    b,c=b.split('=')
    
    x = a.count('|')
    y = b.count('|')
    z = c.count('|')
    
    if x+y==z:
        print(s)
    else:
        if (x-1)+(y+1) == z and (x-1)>0:
            print(crum(x-1)+'+'+crum(y+1)+'='+crum(z))
        elif (x-1)+y == (z+1) and (x-1)>0:
            print(crum(x-1)+'+'+crum(y)+'='+crum(z+1))
        elif (x+1)+(y-1) == z and (y-1)>0:
            print(crum(x+1)+'+'+crum(y-1)+'='+crum(z))
        elif x+(y-1) == (z+1) and (y-1)>0:
            print(crum(x)+'+'+crum(y-1)+'='+crum(z+1))
        elif (x+1)+y == (z-1) and (z-1)>0:
            print(crum(x+1)+'+'+crum(y)+'='+crum(z-1))
        elif x+(y+1) == (z-1) and (z-1)>0:
            print(crum(x)+'+'+crum(y+1)+'='+crum(z-1))
        else:
            print("Impossible")