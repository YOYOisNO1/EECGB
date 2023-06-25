    from sys import stdin
    
    a,b,c = map(int,stdin.readline().split())
    
def damage2():
        for y in range(0,int(c)+1):
            x = int((c - b*y)/a)  
            res = a*x+b*y
            if c == res and x>=0:
                return 'Yes'
        return 'No'
    
    print(damage2())