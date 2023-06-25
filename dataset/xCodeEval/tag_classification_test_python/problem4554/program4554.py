def program4554():
    line=input().split()
    n=int(line[0])
    x=int(line[1])
    y=int(line[2])
    if (x==n/2 or x==n/2+1) and (y==n/2 or y==n/2+1):
        print('NO')
    else:
        print('YES')