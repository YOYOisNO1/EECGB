def program1722():
    a = str(input())
    b = []
    b = a.split()
    x = int(b[0])
    y = int(b[1])
    z = int(b[2])
    
    if x == y and z == 0:
        print('0')
    if x == 0 and y == 0 and z > 0:
        print('?')
    if x + z > y:
        print('+')
    if y + z > x
        print('-')
    else:
        print('?')