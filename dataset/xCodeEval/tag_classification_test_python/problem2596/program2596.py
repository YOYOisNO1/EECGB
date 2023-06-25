    '''
    https://codeforces.com/problemset/problem/1551/D1
    https://codeforces.com/problemset/problem/1551/D2
    
    本题分为简单版本和困难版本，在困难版本中，你需要额外输出具体的方案。
    
    输入 t (≤10) 表示有 t 组数据。
    每组数据输入 n (≤100)、m (m≤100) 和 k (0≤k≤n*m/2)，保证 n*m 是偶数。
    
    请你在一个 n 行 m 列的网格中，放置 n*m/2 个 1*2 大小的骨牌，要求恰好有 k 个是横着放的，其余是竖着放的，且恰好铺满这一 n*m 的网格。
    
    如果存在满足要求的铺设方案，输出 YES，否则输出 NO。
    对于困难版本，如果答案存在，你需要额外输出 n 个长为 m 的由小写字母组成的字符串，表示你铺设的骨牌（多种方案输出任意一种）。要求：两个相邻的单元格拥有相同的字母，表明这两个单元格由同一个骨牌覆盖。具体输出样例见困难版本题目。
    输入
    8
    4 4 2
    2 3 0
    3 2 3
    1 2 0
    2 4 2
    5 2 2
    2 17 16
    2 1 1
    输出
    YES
    YES
    YES
    NO
    YES
    NO
    YES
    NO
    '''
    from itertools import *
    from collections import *
    from math import *
    from heapq import *
    from functools import *
    from bisect import *
    from random import *
    import sys
    from typing import List
    
    
def check(n, m, k):
        # if m<2:return "NO"
        if n & 1:
            k-=m//2
            if k < 0: return "NO"
        elif m & 1:
            if k > m // 2 * n: return "NO"
        if k & 1: return "NO"
        return "YES"
    
    
def solve():
        t = int(sys.stdin.readline())
        for _ in range(t):
            n, m, k = map(int, sys.stdin.readline().split())
            print(check(n, m, k))
    
    
    solve()