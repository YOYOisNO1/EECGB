def program1():
    n = input()
    side = int(ceil(n**0.5))
    if side*(side-1)>n:
        print 4*side
    else:
        print 4*side-2