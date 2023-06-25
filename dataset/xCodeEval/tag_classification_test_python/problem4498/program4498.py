def program4498():
    
    import sys
    import os
    import math
    import re
    
    
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    a = list(input())
    
    if len(a) < 26:
        print('-1')
        exit(0)
    
    m = 0
    for i in range(len(a)):
        if a[i] <= chars[m]:
            a[i] = chars[m]
            m+=1
        if m >25:    
            print(''.join(a))
            exit(0)
        if (len(a)-i-1) < (26-m):
            print('-1')
            exit(0)
    if m < 25:
        print('-1')
        exit(0)
    print(''.join(a))
        