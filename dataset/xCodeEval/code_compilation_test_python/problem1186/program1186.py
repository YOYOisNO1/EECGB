def program1186():
    n = int(input())
    p = 0
    for a in range(1,810):
        for b in range(1,(8101-10*a)):
            c = n - a*1234567-b*123456
            if c>0 c % 1234 == 0:
                p = 1
                break
    
    if p == 1:
        print("YES")
    elif p == 0:
        print("NO")