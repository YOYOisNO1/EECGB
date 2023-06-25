def program3424():
    ﻿from sys import stdin, stdout
    n = map(int, input().split())
    ll = [int(x) for x in stdin.readline().rstrip().split()]
    
    count = 0
    
    idx = -1
    for i in ll:
        idx = idx + 1
        
        if i == 1:
            count += 1
        
        if (idx > 0) and (idx < len(ll)-1):
            if ll[idx-1] == 1 and ll[idx] == 0 and ll[idx+1] == 1:
                count += 1
        
    stdout.write(str(count)+"\n")    