def program4425():
    a=input()
    a=a[0]+a[1:].replace('at','@',1)
    print(a[0]+a[1:-1].replace('dot','.')+a[-1])