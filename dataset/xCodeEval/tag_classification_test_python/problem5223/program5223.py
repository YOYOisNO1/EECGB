    import sys
    import string
    
    console_io = 1
    if console_io:
        inf,ouf = sys.stdin,sys.stdout
    else:
        inf,ouf = open("input.txt","r",1),open("output.txt","w",1)
    #---------------------------------------------------------------------------
    n=0
    s=""
    
def check():
        for s1 in s:
            if not(s1=="7" or s1=="4"):
                return 0
        return 1
    
def count(a, b):
        c = 0
        for i in range(a,b):
            c += string.atoi(s[i])
        return c
        
    n = string.atoi(inf.readline())
    s = inf.read(n)
    
    ouf.write("YES" if check() and count(0,n/2)==count(n/2,n) else "NO")
    
    ouf.close()
    inf.close()