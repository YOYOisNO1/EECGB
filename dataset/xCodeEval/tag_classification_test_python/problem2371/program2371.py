    import atexit
    import io
    import sys
    
    buff = io.BytesIO()
    sys.stdout = buff
    
    
    @atexit.register
def write():
        sys.__stdout__.write(buff.getvalue())
    
    n = input()
    s = input()
    a = 'ACTG'
    ans = int(1e18)
    for i in xrange(len(s)-3):
    	cnt = 0
    	for j in xrange(4):
    		x = int(1e18)
    		x = min(x, -ord(a[j]) + 26 + ord(s[i+j]))
    		x = min(x, ord(a[j]) + 26 - ord(s[i+j]))
    		x = min(x, abs(ord(a[j]) - ord(s[i+j])))
    		cnt += x
    	ans = min(ans, cnt)
    print(ans)