def program1384():
    t = set(x*(x+1)/2 for x in range(1,45001))
    n=input()
    for i in t:
        if n-i in t:
            print('Yes')
            exit()
    print('No')