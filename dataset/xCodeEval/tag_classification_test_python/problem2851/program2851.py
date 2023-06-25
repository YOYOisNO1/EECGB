def program2851():
    x,y = input(), input()
    print(all(a>=b) for a,b in zip(x,y)) * y or "-1"