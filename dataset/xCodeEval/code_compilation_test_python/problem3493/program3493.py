def program3493():
    #!/usr/bin/env python3
    
    import math
    
    #tcs = int(input())
    #for tc in range(tcs):
        n,m,k = [int(i) for i in input().split(' ')]
    
        row = math.ceil(k/(m*2))
        if k%(m*2) is not 0:
            col = math.ceil((k%(m*2))/2)
        else:
            col = m
        lr = 'L' if ((k%(m*2))%2==1) else 'R'
    
        print(row,col,lr)