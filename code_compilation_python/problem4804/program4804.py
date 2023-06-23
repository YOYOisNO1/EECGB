    import sys
    import atexit, io
    buffer = io.BytesIO()
    sys.stdout = buffer
    @atexit.register
def write():
        sys.__stdout__.write(buffer.getvalue())
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
    t=sys.stdin.readline()
    arr = get_ints()
    for n in arr:
    	# print(n)
    	ans=((((n+4)//2)**2)//4)%1000000007
    	print(ans)