def program1045():
    # -*- coding: utf-8 -*-
    """
    Created on Thu Oct  1 11:54:41 2020
    
    @author: Laurent
    """
    import sys
    arg = []
    
    for line in sys.stdin:
        arg.append(line)
    
    n = int(arg[0])
    a = [int(i) for i in arg[1].split(" ")]
    b = [int(i) for i in arg[2].split(" ")]
    
    nbAliceWinMax = min(a[0],b[1]) + min(a[1],b[2])+min(a[2],b[0])
    nbAliceWinMin = max(0,b[0]-a[0]-a[1],b[1]-a[1]-a[2],b[2]-a[2]-a[0])
    
    print(nbAliceWinMin,nbAliceWinMax)