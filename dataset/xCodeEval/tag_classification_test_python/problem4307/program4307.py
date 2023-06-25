def program4307():
    r=int(input())
    if r&1==0 or r<5:
        print(("NO"))
    else:
        print(1,(r-3)//2)