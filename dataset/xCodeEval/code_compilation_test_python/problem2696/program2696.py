def program2696():
    n=-int(input())
    n%=360
    f=360-n if n>=180 else n
    r=[f((n+90*i)%360) for i in range(4)]
    for i in range(4):
        if r[i]==min(r):
            print(i)
            break