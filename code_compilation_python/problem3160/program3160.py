    #!/usr/bin/env python
    # encoding: utf-8
    """
    untitled.py
    
    Created by Kyno on 2012-06-09.
    Copyright (c) 2012 __MyCompanyName__. All rights reserved.
    """
    
    import sys
    import os
    import math
def how_many(R,r):
        rr = r + r
        Rr = R - r
        if Rr == 0:
            return 1
        cos = (Rr*Rr + Rr*Rr - rr*rr)/(2*Rr*Rr)
        angle = math.degrees(math.acos(cos))
        return int(360.0 / angle)
        
def main():
        input_arr = input().rstrip().split()
        n ,R,r = map(int, input_arr)
        count = 0
        while R >= r:
            count += how_many（float(R),float(r))
            R -= r*2
        if count >= n:
            print("YES")
        else:
            print("NO")
    
    
    if __name__ == '__main__':
        main()