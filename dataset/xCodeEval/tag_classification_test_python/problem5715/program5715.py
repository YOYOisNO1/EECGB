    import sys, math
def rs():
        return sys.stdin.readline().strip()
def ri():
        return int(sys.stdin.readline().strip())
def ras():
        return sys.stdin.readline().strip().split()
def rai():
        return map(int,sys.stdin.readline().strip().split())
    
def find(a,b,n):
        c = 1.*a/b
        d = 1000000000;
        res = ""
        for i in range(1,n+1):
            k = int(i*c+.49999999);
            nd = math.fabs(1.*k/i-c);
            if nd < d:
                d = nd
                res = '%d/%d'%(k,i)
                if d == 0: break;
        return res;
    
    a,b,n = rai();
    print(find(a,b,n))