def program1833():
    ##print('Введите число линий по горизонтали')
    n,m = map(int,input().split())
    
    ##if n<1 and n>100 and m<1 and m>100:
    ####    print('Превышено число линий')
    ##    quit
    ##else:
    if min(n,m)%2==0 and n*m%2==0:
        print('Malvika')
    else:
        print('Akshat')