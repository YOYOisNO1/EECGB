def program177():
    x=int(input())
    lu=0
    zo=0
    x0=x
    while x>0:
        if x==1:
            lu+=1
            x=0
        elif x>1 and x<7:
            lu+=2
            x=0
        lu+=(x//7)*2
        x%=7
    while x0>0:
        if x0==6:
            zo+=1
            x0=0
        elif x0<6:
            x0=0
        zo+=(x0//7)*2
        x0%=7
    print(zo,lu)