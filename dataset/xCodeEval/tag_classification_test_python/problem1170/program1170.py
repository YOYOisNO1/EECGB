    start, end = input().split(' ')
    n = int(input())
    
    positions_cw = ['^', '>', 'v', '<']
    positions_ccw = ['^', '<', 'v', '>']
    
    n %= 4
    
def main():
        cw = False
        ccw = False
        for i,pos in enumerate(positions_cw):
            if pos == start:
                if positions_cw[(i + n) % 4] == end:
                    cw = True
                    # return
        for i,pos in enumerate(positions_ccw):
            if pos == start:
                if positions_ccw[(i + n) % 4] == end:
                    ccw = True
                    # return
        if cw and ccw:
            print('undefined')
        elif cw and not ccw:
            print('cw')
        else:
            print('ccw')
    
    if __name__ == '__main__':
        main()