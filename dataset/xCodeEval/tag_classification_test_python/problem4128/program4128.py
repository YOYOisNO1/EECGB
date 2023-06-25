def program4128():
    x = input()
    c='9'
    if x[0] != '9':
        c = str(min(int(x[0]), 9 - int(x[0])))
    print(c) + ''.join(str(min(int(i),9-int(i))) for i in x[1:])