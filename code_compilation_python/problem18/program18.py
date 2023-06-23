def program18():
    import sys
    input = sys.stdin.readline
    import numpy as np 
    
    
    
    length = int(input())
    arr = list(map(int,input().split()))
    
    unique_list = []
    for x in arr: 
            if x not in unique_list: 
                unique_list.append(x)
    print(len(unique_list))
    print(*unique_list)
    
    
    
    