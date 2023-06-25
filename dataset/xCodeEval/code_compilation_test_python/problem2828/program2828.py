def program2828():
    with open(r'Z:\standard input.txt') as inp:
        c = 0
        for line in inp:
            c += 1
            if c == 1:
                x1, y1 = map(int, line.split())
            if c == 2:
                x2, y2 = map(int, line.split())
    
    with open(r'Z:\standard output.txt', 'w') as inf:
        if x1 == x2 and y1 != y2:
            inf.write(str(2*((abs(x2-x1)+2)+(abs(y2-y1)+1))))
        if x1 != x2 and y1 == y2:
            inf.write(str(2*((abs(x2-x1)+1)+(abs(y2-y1)+2))))
        if x1 != x2 and y1 != y2:
            inf.write(str(2*((abs(x2-x1)+1)+(abs(y2-y1)+1))))
        if x1 == x2 and y1 == y2:
            inf.write(str(10))