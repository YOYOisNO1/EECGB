    x = input()
    y = input()
    
    s = int(x) + int(y)
    
def r(x):
        return [i for i in x if i != '0']
    
    sx = r(list(x))
    sy = r(list(y))
    
    if int(''.join(sx)) + int(''.join(sy)) == int(''.join(r(list(str(s))))):
        print('YES')
    else:
        print('NO')
    