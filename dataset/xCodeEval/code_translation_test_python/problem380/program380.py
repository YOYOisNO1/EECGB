def program380():
    n=int(input())+1
    if(n<13):
        s = set()
        for a in range(n):
            for b in range(n-a):
                for c in range(n-a-b):
                    s.add(4*b+9*c+49*a)
        print((len(s)))
    else:
        print((292+(n-12)*49))