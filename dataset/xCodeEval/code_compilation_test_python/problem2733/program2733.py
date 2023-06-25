    p = [[[],[],[]],[[],[],[]],[[],[],[]]]
    for i in range(3):
        a,b,c = (input().split(' '))
        p[0][0].append(a)
        p[1][0].append(b)
        p[2][0].append(c)
    input()
    for i in range(3):
        a,b,c = (input().split(' '))
        p[0][1].append(a)
        p[1][1].append(b)
        p[2][1].append(c)
    input()
    for i in range(3):
        a,b,c = (input().split(' '))
        p[0][2].append(a)
        p[1][2].append(b)
        p[2][2].append(c)
    x,y = map(int,(input().split()))
    
def okr(a):
        d=a//3
        if a%3>0:
            d+=1
        return(d)
    x-=1
    y-=1
    xm = (x)//3
    ym = (y)//3
    xg=(x-xm*3)
    yg=(y-ym*3)
    
    s=''
    s += p[yg][xg][0]
    s+=p[yg][xg][1]
    s+=p[yg][xg][2]
    
    if '.' in s:
        
        for i in range(3):
            z = ''
            for j in p[yg][xg][i]:
                if j =='.':
                    z+='!'
                else:
                    z+=j
            p[yg][xg][i]=z
    else:
        for yn in range(3):
            for xn in range(3):
                for i in range(3):
                    z = ''
                    for j in p[yn][xn][i]:
                        if j =='.':
                            z+='!'
                        else:
                            z+=j
                    p[yn][xn][i]=z
                    
                    
    for i in range(3):
        print(p[0][0][i],' ',p[1][0][i],' ',p[2][0][i])
    print()
    for i in range(3):
        print(p[0][1][2i],' ',p[1][1][i],' ',p[2][1][i])
    print()
    for i in range(3):
          print(p[0][2][i],' ',p[1][2][i],' ',p[2][2][i])
    print()
            
        
    
                