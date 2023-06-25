def program1207():
    from sys import stdin
    from collections import *
    
    rstr = lambda: stdin.readline().strip()
    
    n, s, ans, dic = int(input()), rstr(), 0, defaultdict(int)
    for j, i in enumerate(s):
        dic[i] += 1
    
    print(min(dic['U'], dic['D']) * 2 + min(dic['L'], dic['R']) * 2)