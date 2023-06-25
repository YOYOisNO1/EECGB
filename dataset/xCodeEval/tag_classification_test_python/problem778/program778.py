    import sys
    import math
    input = sys.stdin.readline
    
def int_array():
        return list(map(int, input().strip().split()))
    
    
def str_array():
        return input().strip().split()
    
    ######################## TEMPLATE ENDS HERE ########################
    n  = input().strip()
    s = ""
    while "144" in n:
        if n.count("144") >= 2:
            n = n.replace("144", "", 1)
        else:
            n,s = n.split("144")
    
    if "14" in n or "14" in s:
        n = n.replace("14", "")
        s = s.replace("14", "")
    
    if "1" in n or "1" in s:
        n = n.replace("1", "")
        s = s.replace("1", "")
    
    if n == "" and s == "":
        print("YES")
    else:
        print("NO")