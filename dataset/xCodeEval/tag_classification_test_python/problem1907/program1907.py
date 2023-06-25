def program1907():
    #!/usr/bin/python
    
    import sys
    import math
    
    if __name__=="__main__":
        data = sys.stdin.readline()
        h,m = [int(v) for v in data.split(':')]
        if h >= 12:
            h -= 12
        am = m * 6
        hm = h * 30 + m * 0.5
        print(hm,am)