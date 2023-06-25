    #!/usr/bin/env python
    #untitled.py
    #Author:Abhijith
    #Date:03-Jun-2012
    import sys
    readin=sys.stdin.readline
def readnums():
    	return map(int,readin().split())
    
    n,k=readnums()
    if k>=3*n:
    	print(0)
    else:
    	print(3*n-k)
    