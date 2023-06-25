def program1646():
    #!/bin/python
    from __future__ import print_function
    import sys
    
    n, k = [int(x) for x in sys.stdin.read().split()]
    diferencia = k - n
    counter = 0
    
    
    print(min(k-1,max(k/2,n))-k/2)