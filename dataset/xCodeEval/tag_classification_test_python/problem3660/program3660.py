def program3660():
    n = input()
    print(int(str(int(str(n)[0])+1)+"".join("0") for t in xrange(len(str(n))-1)))-n