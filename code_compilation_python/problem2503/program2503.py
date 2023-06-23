def program2503():
    import math as m
    s = input().split("=")
    left = s[0].split("+")
    a = len(left[0])
    b = len(left[1])
    right = len(s[1])
    print(a,b,right)
    if a+b+right % 2 == 1 or m.fabs(right-a-b) > 2:
        print("Impossible")
    elif a+b == right:
        print(a*"|","+",b*"|","=",right*"|",sep="")
    elif right-a-b == 2:
        right -= 1
        b += 1
        print(a*"|","+",b*"|","=",right*"|",sep="")
    elif right-a-b == -2
        right += 1
        if b > 1:
            b -= 1
        else:
            a -= 1
        print(a*"|","+",b*"|","=",right*"|",sep="")