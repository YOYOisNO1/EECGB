def program1943():
    #!/usr/bin/env python
    #-*- coding: utf-8 -*-
    line = input()
    n, a,b = map(int,line.strip().split())
    ar = map(int,input().strip().split())
    al = map(int,input().strip().split())
    apple = [0]*n
    for i in al:
        apple[i-1] = 2
        for i in ar:
            apple[i-1] = 1
    
    
    print(" ").join(map(str,apple))