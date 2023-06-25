def program3779():
    n=input()
    a = input(" ")
    numZero = a.count('0',0)
    if '1' not in a:
        print(a)
    else:
        a="1"
        for x in range(0,numZero):
            a=a+'0'
        print(a)