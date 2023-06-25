def program1312():
    n=int(input())
    a=input()
    v=[str(len(x)) for x in a.split('w').if len(x)!=0]
    print(len(v))
    print(''.join(v))