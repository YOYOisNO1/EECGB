def program3898():
    a=int(input())
    b = int(input())
    dis = abs(b-a)
    mult,mod = dis//2 ,dis%2*(dis//2+1)
    total = ((mult*(mult+1)))+mod
    print(total)