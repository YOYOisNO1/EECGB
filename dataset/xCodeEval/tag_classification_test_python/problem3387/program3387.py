def program3387():
    line = input()
    temp = line.split()
    n = int(temp[0])
    k = int(temp[1])
    if int(n/k) % 2 ==1:
        print('YES')
    else :
        print('NO')