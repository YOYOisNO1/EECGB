def program568():
    c=[input() for i in range(11)]
    x=[ c[0][i:i+10]     for i in range(0,80,10)]
    for i in x:
        print(c.index(i)-1,end='')