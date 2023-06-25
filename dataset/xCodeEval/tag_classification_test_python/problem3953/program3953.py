    from sys import stdout
    from sys import stdin
def get():
        return stdin.readline().strip()
def getf():
        return [int(i) for i in get().split()]
def put(a, end = "\n"):
        stdout.write(str(a) + end)
def putf(a, sep = " ", end = "\n"):
        stdout.write(sep.join([str(i) for i in a]) + end)
def putff(a, sep = " ", end = "\n"):
        [putf(i, sep, end) for i in a]
    
    #from math import ceil, gcd, factorial as fac
    #from collections import defaultdict as dd
    #from bisect import insort, bisect_left as bl, bisect_right as br
    
def transf(a, w):
        ans = []
        while(a > 0):
            ans.append(a % w)
            a //= w
        return ans[ :: -1]
    
def solve(a, w):
        ans = []
        #print(a)
        p = 0
        for i in range(len(a) - 1, 0, -1):
            if(a[i] + p >= w):
                a[i] = (a[i] + p) % w
                p = 1
            else:
                a[i] += p
                p = 0
            if(a[i] in [0, 1]):
                ans.append(0)
                pass
            elif(a[i] == w - 1):
                p = 1
                ans.append(1)
            else:
                return "NO"
        ans.reverse()
        #print(a)
        #print(ans)
        for i in ans:
            if(i not in [0, 1]):
                return "NO"
        return "YES"
    
def main():
        w, m = getf()
        print(solve([0] + transf(m, w), w))
    main()