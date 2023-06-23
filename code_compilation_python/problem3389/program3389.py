def getans(n):
        if n == 2 :
            return 2
        if n == 3:
            return 4
        return n+getans(n-2)
    print(getans(int(input())))