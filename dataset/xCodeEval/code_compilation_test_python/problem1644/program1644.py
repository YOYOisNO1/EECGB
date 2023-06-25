    rom math import *
    alf = list(reversed('abcdefghijklmnopqrstuvwxyz'))
def adj(a, b):
        return chr(ord(a) - 1) == b
     
    n = int(input())
    s = [i for i in input()]
    for i in range(n):
        for a in alf:
            i = 0
            while i < len(s):
                if s[i] == a and i > 0 and adj(s[i], s[i-1]):
                    s.pop(i)
                elif s[i] == a and i < len(s) - 1 and adj(s[i], s[i+1]):
                    s.pop(i)
                else:
                    i += 1
     
    print(n - len(s))
                