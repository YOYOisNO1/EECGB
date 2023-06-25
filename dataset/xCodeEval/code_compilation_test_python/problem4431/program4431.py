    from __future__ import division, print_function
    
    import os,sys
    from io import BytesIO, IOBase
    
    if sys.version_info[0] < 3:
        from __builtin__ import xrange as range
        from future_builtins import ascii, filter, hex, map, oct, zip
    
    from bisect import bisect_left as lower_bound, bisect_right as upper_bound 
def so():  return int(input())
def st():  return input()
def mj():  return map(int,input().strip().split(" "))
def msj(): return list(map(str,input().strip().split(" ")))
def le():  return list(map(int,input().split()))
def rc():  return map(float,input().split())
def lebe():return list(map(int, input()))
    
def dmain():
        sys.setrecursionlimit(1000000)
        threading.stack_size(1024000)
        thread = threading.Thread(target=main)
        thread.start()
def joro(L):
        return(''.join(map(str, L)))
def joron(L):
        return('\n'.join(map(str, L)))
    
def decimalToBinary(n): return bin(n).replace("0b","")
    
    
def isprime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
def npr(n, r):
        return factorial(n) // factorial(n - r) if n >= r else 0
     
     
def ncr(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r)) if n >= r else 0
     
     
def lower_bound(li, num):
        answer = -1
        start = 0
        end = len(li) - 1
     
        while (start <= end):
            middle = (end + start) // 2
            if li[middle] >= num:
                answer = middle
                end = middle - 1
            else:
                start = middle + 1
        return answer  # min index where x is not less than num
     
     
def upper_bound(li, num):
        answer = -1
        start = 0
        end = len(li) - 1
     
        while (start <= end):
            middle = (end + start) // 2
     
            if li[middle] <= num:
                answer = middle
                start = middle + 1
     
            else:
                end = middle - 1
        return answer  # max index where x is not greater than num
def tir(a,b,c):
        if(0==c):
            return 1
        if(len(a)<=b):
            return 0
        
        if(c!=-1):
            return (tir(a,1+b,c+a[b]) or tir(a,b+1,c-a[b]) or tir(a,1+b,c)) 
            
            
        else:
            return (tir(a,1+b,a[b]) or tir(a,b+1,-a[b]) or tir(a,1+b,-1))
       
     
def abs(x):
        return x if x >= 0 else -x
     
     
def binary_search(li, val, lb, ub):
        # print(lb, ub, li)
        ans = -1
        while (lb <= ub):
            mid = (lb + ub) // 2
            # print('mid is',mid, li[mid])
            if li[mid] > val:
                ub = mid - 1
            elif val > li[mid]:
                lb = mid + 1
            else:
                ans = mid  # return index
                break
        return ans
     
     
def kadane(x):  # maximum sum contiguous subarray
        sum_so_far = 0
        current_sum = 0
        for i in x:
            current_sum += i
            if current_sum < 0:
                current_sum = 0
            else:
                sum_so_far = max(sum_so_far, current_sum)
        return sum_so_far
    
                        
def pref(li):
        pref_sum = [0]
        for i in li:
            pref_sum.append(pref_sum[-1] + i)
        return pref_sum
     
    
            
            
def SieveOfEratosthenes(n):
        prime = [True for i in range(n + 1)]
        p = 2
        li = []
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
     
        for p in range(2, len(prime)):
            if prime[p]:
                li.append(p)
        return li
     
     
def primefactors(n):
        factors = []
        while (n % 2 == 0):
            factors.append(2)
            n //= 2
        for i in range(3, int(sqrt(n)) + 1, 2):  # only odd factors left
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 2:  # incase of prime
            factors.append(n)
        return factors
             
        
def read():
        sys.stdin  = open('input.txt', 'r')  
        sys.stdout = open('output.txt', 'w') 
def tr(n):
        return n*(n+1)//2
    boi=int(1e9+7)
    doi=int(1e9+7)
    hoi=int(6e5+5)
    
    poi=int(1e5+5)
    
    y="YES"
    n="NO"
    
def bulli(x):
        return bin(x).count('1')
    
    import sys
    
    
    f=[0]*(hoi)
    r=[0]*(hoi)
    d=[]
    for i in range(poi):
        d.append([])
    L=[0]*poi
    M=[0]*poi
    
        
        
    
            
        
        
    
            
            
        
    
def ty(a,b):
        rr=1
        while(b):
            if(b%2):
                rr=(rr*a)%boi
            b=b//2
            a=a*a%boi
        return rr
def inv(a):
        re=1
        for i in range(1,1+a):
            re=(re*i)%boi
        re=ty(re,boi-2)
        return re
def ncr(m,k):
        if(m<0 or k<0 or k>m):
            return 0
        return f[m]*r[k]%boi*r[m-k]%boi
def gosa(a,b):
        if(0!=b):
            return gosa(b,a%b)
        return a
    
    
        
        
        
    
def iu():
        import sys
        import math as my
        import functools
        import bisect as bs
        input=sys.stdin.readline
        from collections import deque, defaultdict
        '''f[0]=1
        for i in range(1,hoi):
            f[i]=(f[i-1]*i)%boi
        r[hoi-1]=ty(f[hoi-1],boi-2)
        for i in range(hoi-2,-1,-1):
            r[i]=r[i+1]*(i+1)%boi'''
        z=0
        m=so()
        for i in range(poi-1,0,-1):
            for j in range(i,poi,i):
                d[j].append(i)
        for i in range(1,1+m):
            r=m-i
            s=len(d[r])
            for j in range(s):
                M[j]=r//(d[r][j])-1
                for k in range(j):
                    if(not d[r][k]%d[r][j]):
                        M[j]=M[j]-M[k]
                z=z+M[j]*i*d[r][j]//gosa(d[r][j],i)%boi
        print(z%boi)
        
        
        
                
        
        
def main():
        for i in range(1):
            #print("Case #"+str(i+1)+": ",end="")
            iu()
            
            
            
            
                   
        
                
        
        
        
        
        
        
        
        
        
            
                    
                
            
            
        
        
                
        
        
        
        
        
        
            
                
            
        
        
        
        
            
                
        
            
            
            
    
        
        
        
        
            
            
        
            
        
        
                
        
        
        
                    
                
                
        
            
    
                    
        
            
            
    
                
                        
                    
                        
                        
                        
                        
                        
                        
            
                    
            
            
           
        
               
              
              
                    
                
            
                    
        
            
            
            
           
                
                    
            
    
    
    
    
    # region fastio
    # template taken from https://github.com/cheran-senthil/PyRival/blob/master/templates/template.py
    
    BUFSIZE = 8192
    
    
    class FastIO(IOBase):
        newlines = 0
    
    def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None
    
    def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()
    
    def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()
    
    def flush(self):
            if self.writable:
                os.write(self._fd, self.buffer.getvalue())
                self.buffer.truncate(0), self.buffer.seek(0)
    
    
    class IOWrapper(IOBase):
    def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    
    
def print(*args, **kwargs):
        """Prints the values to a stream, or to sys.stdout by default."""
        sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
        at_start = True
        for x in args:
            if not at_start:
                file.write(sep)
            file.write(str(x))
            at_start = False
        file.write(kwargs.pop("end", "\n"))
        if kwargs.pop("flush", False):
            file.flush()
    
    
    if sys.version_info[0] < 3:
        sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
    else:
        sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    
    # endregion
    
    
    if __name__ == "__main__":
        #read()
        main()
        #dmain()
    
    # Comment Read()