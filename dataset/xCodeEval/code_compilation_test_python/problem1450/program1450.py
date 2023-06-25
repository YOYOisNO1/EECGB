def program1450():
    n=[int(i) for i in input().split()]
    if(n[-1]%2==0):
        print(n[-1])
    else:
        print(n[-2])