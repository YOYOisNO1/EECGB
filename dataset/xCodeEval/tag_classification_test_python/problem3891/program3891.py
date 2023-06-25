def program3891():
    # bsdk idhar kya dekhne ko aaya hai, khud kr!!!
    # import math
    # from itertools import *
    # import random
    # import calendar
    # import datetime
    # import webbrowser
    
    # f = open("input.txt", 'r')
    # g = open("output.txt", 'w')
    # n, m = map(int, f.readline().split())
    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    length = 0
    done = set()
    for i in arr:
        if i not in done:
            done.add(i)
            length += i
        else:
            while i in done:
                i -= 1
            if i < 0:
                continue
            else:
                done.add(i)
                length += i
    print(length)