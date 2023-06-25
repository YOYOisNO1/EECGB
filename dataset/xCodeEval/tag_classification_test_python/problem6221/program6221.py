def program6221():
    r1, c1, r2, c2 = map(int, input().split())
    # rook
    print(('1') if (r2 == r1 or c2 == c1) else '2'),
    # bishop
    if (r1 + c1) % 2 != (r2 + c2) % 2:
    	print('0'),
    elif abs(r2 - r1) == abs(c2 - c1):
    	print('1'),
    else:
    	print('2')
    # king
    print((max(abs(r2) - r1),  abs(c2 - c1))),