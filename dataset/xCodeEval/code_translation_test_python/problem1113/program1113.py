def program1113():
    from sys import *
    a, b, m, r0 = map(int, stdin.readline().split())
    was = {}
    r = r0
    i = 1
    while True:
        if r in was:
            print(i - was[r])
            exit(0)
        was[r] = i
        i += 1
        r = (a * r + b) % m
        
        
        
        