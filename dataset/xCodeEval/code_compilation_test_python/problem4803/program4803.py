    import atexit, io, sys
     
    buffer = io.BytesIO()
    sys.stdout = buffer
    
    @atexit.register
def write():
        sys.__stdout__.write(buffer.getvalue())
    
    n = int(input())
    m = input().split()
    for x in m:
    	x = int(x)
    	print( (((((x+4)//2)**2)//4)%1000000007) )