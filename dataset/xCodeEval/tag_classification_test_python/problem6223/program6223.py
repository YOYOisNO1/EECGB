def program6223():
    a,b=map(int,input().split())
    if(a==b):
        print('Equal')
        exit()
    import math
    
    lcm=(a*b)//(math.gcd(a,b))
    if(a<b):
        da=(lcm//a)-1
        ma=lcm//b
        if(da>ma):
            print('Dasha')
        elif(da<ma):
            print('Masha')
        else:
            print('Equal')
    else:
        da=(lcm//a)
        ma=(lcm//b)-1
        if(da>ma):
            print('Dasha')
        elif(da<ma):
            print('Masha')
        else:
            print('Equal')
        