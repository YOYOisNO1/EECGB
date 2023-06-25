    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    
    import sys
    import fractions
    
    DEBUG = 0
    
def ReadIn():
        data = [int(x) for x in sys.stdin.read().split()]
        offset = 0
        while offset < len(data):
            board = data[offset], data[offset + 1]
            offset += 2
            center = data[offset], data[offset + 1]
            offset += 2
            ratio = data[offset], data[offset + 1]
            offset += 2
            yield board, center, ratio
    
def Solve(board, center, ratio):
        if DEBUG:
            print(locals())
        gcd = fractions.gcd(*ratio)
        if DEBUG:
            print('gcd ='), gcd
        ratio = tuple(map(lambda x: x // gcd, ratio))
        if DEBUG:
            print('ratio ='), ratio
        times = min(map(lambda x, y: x // y, board, ratio))
        if DEBUG:
            print('times ='), times
        rect = tuple(map(lambda x: x * times, ratio))
        if DEBUG:
            print('rect ='), rect
        lowerLeft = map(lambda x, y: y - (x + 1) // 2, rect, center)
        upperRight = map(lambda x, y: y + x // 2, rect, center)
        if DEBUG:
            print('ans ='), lowerLeft, upperRight
        for idx in xrange(2):
            if lowerLeft[idx] < 0:
                upperRight[idx] -= lowerLeft[idx]
                lowerLeft[idx] = 0
            if upperRight[idx] > board[idx]:
                lowerLeft[idx] -= upperRight[idx] - board[idx]
                upperRight[idx] = board[idx]
        
        if DEBUG:
            print('mod ans ='), lowerLeft + upperRight
        
        print(' ').join(['%d'] * 4) % tuple(lowerLeft + upperRight)
    
        
    
    if __name__ == '__main__':
        for board, center, ratio in ReadIn():
            Solve(board, center, ratio)