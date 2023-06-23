    # -*- coding: utf-8 -*-
def writeline(l): print " ".join(map(str, l))
def readline(): return map(int, input().split())
def readint(): return int(input(), 10)
    
    
def main():
        n, t, k, n = readline()
        print("NO") if (d // t + 1) * k >= n else "YES"
    
    
    main()