    import sys
    testing = len(sys.argv) == 4 and sys.argv[3] == "myTest"
    interactive = False
    if testing:
        cmd = sys.stdout
        from time import time
        start_time = int(round(time() * 1000)) 
        readAll = open(sys.argv[1], 'r').read
        sys.stdout = open(sys.argv[2], 'w')
    else:
        readAll = sys.stdin.read
    
    # ############ ---- I/O Functions ---- ############
    
    class InputData:
    def __init__(self):
            self.lines = readAll().split('\n')
            self.n = len(self.lines)
            self.ii = -1
    def input(self):
            self.ii += 1
            assert self.ii < self.n
            return self.lines[self.ii]
    
    flush = sys.stdout.flush
    if interactive and not testing:
        input = sys.stdin.readline
    else:
        inputData = InputData()
        input = inputData.input
    
def intin():
        return(int(input()))
def intlin():
        return(list(map(int,input().split())))
def chrin():
        return(list(input()))
def strin():
        return input()
def lout(l, sep="\n", toStr=True):
        print(sep.join(map(str, l) if toStr else l))
def dout(*args, **kargs):
        if not testing: return
        if args: print(args[0] if len(args)==1 else args)
        if kargs: print([(k,v) for k,v in kargs.items()])
def ask(q):
        sys.stdout.write(str(q)+'\n')
        flush()
        return intin()
    # xrange = range
    # ############ ---- I/O Functions ---- ############
    
    # from math import ceil
    from collections import defaultdict as ddict, Counter
    # from heapq import *
    # from Queue import Queue
    mod = 10**9+7
    
    K = 2*10**5
    pow2 = [1]*(K+1)
    for i in xrange(1,K+1):
        pow2[i] = (pow2[i-1]*2)%mod
    dout(pow2)
    modb = format(mod-2, 'b')[::-1]
    M = len(modb)
def main():
        n,k = intlin()
        if n%2 == 0:
            a = (pow(pow2[n],k,mod)-pow(pow2[n-1]-1,k,mod))%mod
            b = (pow2[n-1]+1)%mod
            powM = [1]*M
            powM[0] = b
            for m in xrange(1,M):
                powM[m] = (powM[m-1]*powM[m-1])%mod
            ib = 1
            for i in xrange(M):
                if modb[i] == '1':
                    ib = (ib*powM[i])%mod
            return (pow(pow2[n-1]-1,k,mod)+a*ib)%mod
        else:
            return pow(pow2[n-1]+1,k,mod)
    
    anss = []
    for _ in xrange(intin()):
        anss.append(main())
        # anss.append("YES" if main() else "NO")
    lout(anss)
    
    if testing:
        sys.stdout = cmd
        print(int(round(time() * 1000))  - start_time)