def program1791():
    a,b = [int(x) for x in input().split()] 
    if abs(a-b) <= 1:
        print(‘YES’)
    else:
        print(‘NO’)