def program2874():
    d = ['U', 'RD', 'LRD', 'LD', 'UDR', 'UDLR', 'UDL', 'UR', 'UDLR', 'UL']
    n, v = int(input()), set('UDLR')
    for ch in input():
        v &= set(d[ord(ch) - ord('0')])
    print('NO' if v else 'YES')