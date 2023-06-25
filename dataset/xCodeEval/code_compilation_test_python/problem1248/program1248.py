def program1248():
    a,b,c = map(int, input().split())
    if abs(b-a)!>2:
        print(a+b+2*c)
    else:
        print(min(a,b)*2+1+2*c)