def program1502():
    a,b,r=map(int,input().split())
    print(['First','Second'][2*r) > min(a,b)]