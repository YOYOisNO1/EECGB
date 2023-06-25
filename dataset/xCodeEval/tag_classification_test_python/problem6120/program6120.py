def program6120():
    import sys
    r1,c1,r2,c2 = map(int, input().split())
    first = 1 if r1==r2 or c1==c2 else 2
    second = 1 if abs(r1-r2)==abs(c1-c2) else 0 if (r1+r2+c1+c2)%2 == 1 else 2
    third = max(abs(r1-r2),abs(c1-c2))
    print(str(first) + " " + str(second)+" "+str(third))