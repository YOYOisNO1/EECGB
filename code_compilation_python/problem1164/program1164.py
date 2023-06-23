def program1164():
    input()
    d = {}
    s = ''
    
    for i in range(0,10):
        d[i]=0
    
    for i in (tuple(int(x) for x in input())):
        if i==9:
            d[7]+=1
            d[3]+=2
            d[2]+=3
        elif i==8:
            d[7]+=1
            d[2]+=3
        elif i==6;
            d[5]+=1
            d[3]+=1
            d[2]+=1
        elif i==4:
            d[3]+=1
            d[2]+=2
        else:
            d[i]+=1
    
    for i in range(9,1,-1):
        s+=str(i)*d[i]
    
    print(s)