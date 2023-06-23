    ﻿#!/usr/bin/env python3
    import sys
    
    
def main(x, y, z, t1, t2, t3):
        lift_time = (abs(z-x)*t2+t3) + (abs(x-y)*t2+t3)
        walk_time = (abs(x-y)) * t1
        return 'YES' if lift_time <= walk_time else 'NO'
    
    
    if __name__ == '__main__':
        print(main(*[int(x) for x in sys.argv[1].split()]))