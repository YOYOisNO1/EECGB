def program3736():
    n = int(input())
    loops = [1,0,0,0,1,0,1,0,2,1]
    power = 0
    num = 0
    if n > 36:
        print(-1)
    elif n==0:
        print(1)
    else:
        while n != 0:
            if n>=2:
                num += 8*10**power
                power+=1
                n-=2
            elif n == 1:
                num += 4*10**power
                power += 1
                n-=1
        if n!= 0:
            print(-1)
        else:
            print(num)
    
    
    