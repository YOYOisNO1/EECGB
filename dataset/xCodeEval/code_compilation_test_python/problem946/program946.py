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
    # from collections import defaultdict as ddict, Counter
    # from heapq import *
    # from Queue import Queue
    mod = 10**9+7
    # N = 2*10**5
    # facts = [1]*(N+1)
    # for i in xrange(1,N):
    #     facts[i] = (facts[i-1]*i)%mod
    # dout(facts)
    
# def nCr(n,r):
    #     return facts[n] / (facts[r]*facts[n-r])
    K = 2*10**5
    pow2 = [1]*(K+1)
    for i in xrange(1,K+1):
        pow2[i] = (pow2[i-1]*2)%mod
    dout(pow2)
def main():
        n,k = intlin()
        if n%2 == 0:
            return pow(pow2[n-1]-1,k,mod)+(pow(2,n,k-(2**(n-1)-1)**k)/((2**(n-1))+1)
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