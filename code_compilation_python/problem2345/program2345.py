def program2345():
    x = input()
    y = input()
    r = [i<j for i,j in zip(x,y)]
    if any(r):
        return -1
    else:
        return y