def program520():
    R=input
    b=map(R," "*int(R()[:2]))
    S=lambda b:sum('S'in i for i in b)
    print len(b)*len(b[0])-S(b)*S(zip(*b))