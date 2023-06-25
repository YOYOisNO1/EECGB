    #!/usr/bin/python2
    # -*- coding: utf-8 -*-
    
    import sys
    import os
    
def main():
        s = sys.stdin.readline().strip()
        n = int(s[:-1])
        p = s[-1]
        n -= 1
        d = "fedabc"
        print(1) + n / 4 * 16 + n % 2 * 7 + d.index(p)
    
    if __name__ == '__main__':
        main()