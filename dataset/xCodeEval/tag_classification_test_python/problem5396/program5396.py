    import sys, os, io
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(sys.stdin.readline())
def ria(): return list(map(int, sys.stdin.readline().split()))
def ws(s): sys.stdout.write(s + '\n')
def wi(n): sys.stdout.write(str(n) + '\n')
def wia(a): sys.stdout.write(' '.join([str(x) for x in a]) + '\n')
    import math,datetime,functools,itertools,operator,bisect,fractions,statistics
    from collections import deque,defaultdict,OrderedDict,Counter
    from fractions import Fraction
    from decimal import Decimal
    from sys import stdout
    from heapq import heappush, heappop, heapify ,_heapify_max,_heappop_max,nsmallest,nlargest
    # sys.setrecursionlimit(111111) 
    INF=999999999999999999999999
    alphabets="abcdefghijklmnopqrstuvwxyz"
    class SortedList:
    def __init__(self, iterable=[], _load=200):
            """Initialize sorted list instance."""
            values = sorted(iterable)
            self._len = _len = len(values)
            self._load = _load
            self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
            self._list_lens = [len(_list) for _list in _lists]
            self._mins = [_list[0] for _list in _lists]
            self._fen_tree = []
            self._rebuild = True
     
    def _fen_build(self):
            """Build a fenwick tree instance."""
            self._fen_tree[:] = self._list_lens
            _fen_tree = self._fen_tree
            for i in range(len(_fen_tree)):
                if i | i + 1 < len(_fen_tree):
                    _fen_tree[i | i + 1] += _fen_tree[i]
            self._rebuild = False
     
    def _fen_update(self, index, value):
            """Update `fen_tree[index] += value`."""
            if not self._rebuild:
                _fen_tree = self._fen_tree
                while index < len(_fen_tree):
                    _fen_tree[index] += value
                    index |= index + 1
     
    def _fen_query(self, end):
            """Return `sum(_fen_tree[:end])`."""
            if self._rebuild:
                self._fen_build()
     
            _fen_tree = self._fen_tree
            x = 0
            while end:
                x += _fen_tree[end - 1]
                end &= end - 1
            return x
     
    def _fen_findkth(self, k):
            """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
            _list_lens = self._list_lens
            if k < _list_lens[0]:
                return 0, k
            if k >= self._len - _list_lens[-1]:
                return len(_list_lens) - 1, k + _list_lens[-1] - self._len
            if self._rebuild:
                self._fen_build()
     
            _fen_tree = self._fen_tree
            idx = -1
            for d in reversed(range(len(_fen_tree).bit_length())):
                right_idx = idx + (1 << d)
                if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                    idx = right_idx
                    k -= _fen_tree[idx]
            return idx + 1, k
     
    def _delete(self, pos, idx):
            """Delete value at the given `(pos, idx)`."""
            _lists = self._lists
            _mins = self._mins
            _list_lens = self._list_lens
     
            self._len -= 1
            self._fen_update(pos, -1)
            del _lists[pos][idx]
            _list_lens[pos] -= 1
     
            if _list_lens[pos]:
                _mins[pos] = _lists[pos][0]
            else:
                del _lists[pos]
                del _list_lens[pos]
                del _mins[pos]
                self._rebuild = True
     
    def _loc_left(self, value):
            """Return an index pair that corresponds to the first position of `value` in the sorted list."""
            if not self._len:
                return 0, 0
     
            _lists = self._lists
            _mins = self._mins
     
            lo, pos = -1, len(_lists) - 1
            while lo + 1 < pos:
                mi = (lo + pos) >> 1
                if value <= _mins[mi]:
                    pos = mi
                else:
                    lo = mi
     
            if pos and value <= _lists[pos - 1][-1]:
                pos -= 1
     
            _list = _lists[pos]
            lo, idx = -1, len(_list)
            while lo + 1 < idx:
                mi = (lo + idx) >> 1
                if value <= _list[mi]:
                    idx = mi
                else:
                    lo = mi
     
            return pos, idx
     
    def _loc_right(self, value):
            """Return an index pair that corresponds to the last position of `value` in the sorted list."""
            if not self._len:
                return 0, 0
     
            _lists = self._lists
            _mins = self._mins
     
            pos, hi = 0, len(_lists)
            while pos + 1 < hi:
                mi = (pos + hi) >> 1
                if value < _mins[mi]:
                    hi = mi
                else:
                    pos = mi
     
            _list = _lists[pos]
            lo, idx = -1, len(_list)
            while lo + 1 < idx:
                mi = (lo + idx) >> 1
                if value < _list[mi]:
                    idx = mi
                else:
                    lo = mi
     
            return pos, idx
     
    def add(self, value):
            """Add `value` to sorted list."""
            _load = self._load
            _lists = self._lists
            _mins = self._mins
            _list_lens = self._list_lens
     
            self._len += 1
            if _lists:
                pos, idx = self._loc_right(value)
                self._fen_update(pos, 1)
                _list = _lists[pos]
                _list.insert(idx, value)
                _list_lens[pos] += 1
                _mins[pos] = _list[0]
                if _load + _load < len(_list):
                    _lists.insert(pos + 1, _list[_load:])
                    _list_lens.insert(pos + 1, len(_list) - _load)
                    _mins.insert(pos + 1, _list[_load])
                    _list_lens[pos] = _load
                    del _list[_load:]
                    self._rebuild = True
            else:
                _lists.append([value])
                _mins.append(value)
                _list_lens.append(1)
                self._rebuild = True
     
    def discard(self, value):
            """Remove `value` from sorted list if it is a member."""
            _lists = self._lists
            if _lists:
                pos, idx = self._loc_right(value)
                if idx and _lists[pos][idx - 1] == value:
                    self._delete(pos, idx - 1)
     
    def remove(self, value):
            """Remove `value` from sorted list; `value` must be a member."""
            _len = self._len
            self.discard(value)
            if _len == self._len:
                raise ValueError('{0!r} not in list'.format(value))
     
    def pop(self, index=-1):
            """Remove and return value at `index` in sorted list."""
            pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
            value = self._lists[pos][idx]
            self._delete(pos, idx)
            return value
     
    def bisect_left(self, value):
            """Return the first index to insert `value` in the sorted list."""
            pos, idx = self._loc_left(value)
            return self._fen_query(pos) + idx
     
    def bisect_right(self, value):
            """Return the last index to insert `value` in the sorted list."""
            pos, idx = self._loc_right(value)
            return self._fen_query(pos) + idx
     
    def count(self, value):
            """Return number of occurrences of `value` in the sorted list."""
            return self.bisect_right(value) - self.bisect_left(value)
     
    def __len__(self):
            """Return the size of the sorted list."""
            return self._len
     
    def __getitem__(self, index):
            """Lookup value at `index` in sorted list."""
            pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
            return self._lists[pos][idx]
     
    def __delitem__(self, index):
            """Remove value at `index` from sorted list."""
            pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
            self._delete(pos, idx)
     
    def __contains__(self, value):
            """Return true if `value` is an element of the sorted list."""
            _lists = self._lists
            if _lists:
                pos, idx = self._loc_left(value)
                return idx < len(_lists[pos]) and _lists[pos][idx] == value
            return False
     
    def __iter__(self):
            """Return an iterator over the sorted list."""
            return (value for _list in self._lists for value in _list)
     
    def __reversed__(self):
            """Return a reverse iterator over the sorted list."""
            return (value for _list in reversed(self._lists) for value in reversed(_list))
     
    def __repr__(self):
            """Return string representation of sorted list."""
            return 'SortedList({0})'.format(list(self))
        
    class SegTree:
        
    def __init__(self, n):
            self.N = 1 << n.bit_length()
            self.tree = [0] * (self.N<<1)
        
    def update(self, i, j, v):
            i += self.N
            j += self.N
            while i <= j:
                if i%2==1: self.tree[i] += v
                if j%2==0: self.tree[j] += v
                i, j = (i+1) >> 1, (j-1) >> 1
        
    def query(self, i):
            v = 0
            i += self.N
            while i > 0:
                v += self.tree[i]
                i >>= 1
            return v
    
def SieveOfEratosthenes(limit):
        """Returns all primes not greater than limit."""
        isPrime = [True]*(limit+1)
        isPrime[0] = isPrime[1] = False
        primes = []
        for i in range(2, limit+1):
            if not isPrime[i]:continue
            primes += [i]
            for j in range(i*i, limit+1, i):
                isPrime[j] = False
        return primes
    from collections import Counter
    
    
def gcd(x, y):
        """greatest common divisor of x and y"""
        while y:
            x, y = y, x % y
        return x
    
    
def memodict(f):
        """memoization decorator for a function taking a single argument"""
        class memodict(dict):
        def __missing__(self, key):
                ret = self[key] = f(key)
                return ret
    
        return memodict().__getitem__
    
    
def pollard_rho(n):
        """returns a random factor of n"""
        if n & 1 == 0:
            return 2
        if n % 3 == 0:
            return 3
    
        s = ((n - 1) & (1 - n)).bit_length() - 1
        d = n >> s
        for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
            p = pow(a, d, n)
            if p == 1 or p == n - 1 or a % n == 0:
                continue
            for _ in range(s):
                prev = p
                p = (p * p) % n
                if p == 1:
                    return gcd(prev - 1, n)
                if p == n - 1:
                    break
            else:
                for i in range(2, n):
                    x, y = i, (i * i + 1) % n
                    f = gcd(abs(x - y), n)
                    while f == 1:
                        x, y = (x * x + 1) % n, (y * y + 1) % n
                        y = (y * y + 1) % n
                        f = gcd(abs(x - y), n)
                    if f != n:
                        return f
        return n
    
    
    @memodict
def prime_factors(n):
        """returns a Counter of the prime factorization of n"""
        if n <= 1:
            return Counter()
        f = pollard_rho(n)
        return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)
    
    
def distinct_factors(n):
        """returns a list of all distinct factors of n"""
        factors = [1]
        for p, exp in prime_factors(n).items():
            factors += [p**i * factor for factor in factors for i in range(1, exp + 1)]
        return factors
    
    
def all_factors(n):
        """returns a sorted list of all distinct factors of n"""
        small, large = [], []
        for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
            if not n % i:
                small.append(i)
                large.append(n // i)
        if small[-1] == large[-1]:
            large.pop()
        large.reverse()
        small.extend(large)
        return small
    
    N = 200000
     
    # array to store inverse of 1 to N 
    factorialNumInverse = [None] * (N + 1) 
     
    # array to precompute inverse of 1! to N! 
    naturalNumInverse = [None] * (N + 1) 
     
    # array to store factorial of  
    # first N numbers 
    fact = [None] * (N + 1) 
     
    # Function to precompute inverse of numbers 
def InverseofNumber(p): 
        naturalNumInverse[0] = naturalNumInverse[1] = 1
        for i in range(2, N + 1, 1): 
            naturalNumInverse[i] = (naturalNumInverse[p % i] * 
                                    (p - int(p / i)) % p) 
    # Function to precompute inverse  
    # of factorials 
def InverseofFactorial(p): 
        factorialNumInverse[0] = factorialNumInverse[1] = 1
      
        # precompute inverse of natural numbers 
        for i in range(2, N + 1, 1): 
            factorialNumInverse[i] = (naturalNumInverse[i] * 
                                      factorialNumInverse[i - 1]) % p 
      
    # Function to calculate factorial of 1 to N 
def factorial(p): 
        fact[0] = 1
      
        # precompute factorials 
        for i in range(1, N + 1): 
            fact[i] = (fact[i - 1] * i) % p 
      
    # Function to return nCr % p in O(1) time 
def nCr(N, R, p): 
          
        # n C r = n!*inverse(r!)*inverse((n-r)!) 
        ans = ((fact[N] * factorialNumInverse[R])% p * 
                          factorialNumInverse[N - R])% p 
        return ans 
def main():
    
        mod=1000000007
        InverseofNumber(mod)
        InverseofFactorial(mod)
        factorial(mod)
        starttime=datetime.datetime.now()
        if(os.path.exists('input.txt')):
            sys.stdin = open("input.txt","r")
            sys.stdout = open("output.txt","w")
        
        tc=1
        
        # Did you look at the constraints dummy?
        # 1.Greedy?
        # 2.DP?
        # 3.Binary Search?(Monotonic? any one directed order in which we have to perform something?)
        # 4.Graph? Bipartitenes???
        # 5.Number Theory?(GCD subtraction?)
        # 6.Bruteforce?(Redundant part of N which may not give answer?Constraints?)
        # 7.Range Queries?
        # 8.Any Equivalency?(We have A and B and have to do 
        #   something between them maybe difficult if there was A~C and C~B then A~B
        #   C could be max or min or some other thing)
        # 9.Reverse Engineering?(From Answer to quesn or last step to first step)
        #10.Constructive? Mod?
    
        tc=ri()
        for _ in range(tc):
            n,k=ria()
            
            # CONDITION --> a1 & a2 & a3 & … & an >= a1 ⊕ a2 ⊕ a3 ⊕ … ⊕ an
            
            # LOGIC -
            # Case 1- If n is odd
            # Lets consider ith bit of all numbers
            # 1. If ith bit is set in all numbers
            #    &  gives 1
            #    ⊕  gives 1
            #
            # 2. If ith bit occurs odd number of times but not n times
            #    &  gives 0
            #    ⊕  gives 1
            #
            # 3. If ith bit occurs even number of times but not n times
            #    &  gives 0
            #    ⊕  gives 0
            #
            # Conclusion incase when n is odd 1 and 3 will satisfy given condition
            # which shows that we can only make AND atmost equal to XOR when n is odd but never more than xor
            # Number Of Ways to make this happen = 1 (1 way to set all bits 1)  + [nC0 +nC2 +nC4 ...nCn-1] (total ways to choose even number of bits but not all bits)
            # Total ways = (number of ways for 1 bit)^k
            #            = (1 + [nC0 +nC2 +nC4 ...nCn-1])^k 
            #      
            # Case 2- If n is even
            # Lets consider ith bit of all numbers
            # 1. If ith bit is set in all numbers
            #    &  gives 1
            #    ⊕  gives 0
            #
            # 2. If ith bit occurs odd number of times but not n times
            #    &  gives 0
            #    ⊕  gives 1
            #
            # 3. If ith bit occurs even number of times but not n times
            #    &  gives 0
            #    ⊕  gives 0
            #
            # Conclusion incase when n is even 1 and 3 will satisfy given condition
            # Using 1 we can make AND more than XOR then we dont care about bits to the right side of ith bit
            # Using 3 we can make AND and XOR equal
            # Number Of Ways to make this happen = Ways to do 1 + Ways to do 3
            # Ways to do 3 is similar to odd we just have to make = [nC0 +nC2 +nC4 ...nCn-2] (total ways to choose even number of bits but not all bits)
            # Ways to do 1 is as follows : 
            # Let us set kth bit for all numbers which can be done in 1 way then we can choose rest k-1 bits on right of kth bit to be anything
            # This will be equal to 1*((2^n)^(k-1))
            # Similarly we can now do this for k-1 th bit set it and choose rest k-2 bits to its right
            # This will be equal to 1*((2^n)^(k-2))
            #
            # MOST IMPORTANT STEP-
            # We can have to think of a way where every possible 1 and 3 condition will hold        
            # We can do set ith bit off all numbers for every i from k to 0
            # When k is zero all bits are equal condition is automatically held
            # k to i+1 bits are equal , ith bit is more as it is all set , i-1 th to 1st bit can be anything
            # The above line is to be considered for all i from k to 0
            
            if n%2:
                equal=0
                for i in range(0,n,2):
                    equal=(equal+nCr(n,i,mod))%mod
                wi(pow(equal+1,k,mod))
            
            else:
                ans=0
                equal=0
                for i in range(0,n,2):
                    equal=(equal+nCr(n,i,mod))%mod
                eq=1
                twopown=pow(2,n,mod)
                for i in range(k,-1,-1):
                    greater=1 
                    if i: greater=(pow(twopown,i-1,mod))%mod
                    ans=(ans+eq*greater)%mod
                    eq=(equal*eq)%mod
                wi(ans)
                
                
            
               
            
            
             
                                    
                    
                
    
    
            
            
    
            
            
    
            
            
            
                
            
            
                
                    
    
                
                
                    
                
                
                
                
            
            
           
             
            
    
            
            
                        
                            
    
                        
               
                         
                
            
                    
            
            
                
            
            
            
            
            
    
        
            
            
            
                    
                    
            
            
            
        
    
            
            
            
    
            
                                 
            
            
            
                
            
            
                         
            
            
                        
            
                         
                        
                        
                    
                    
                        
                    
            
            
                
                       
            
                        
    
            
            
                    
                
                
        
                
                            
            
        
    
            
        #<--Solving Area Ends
        endtime=datetime.datetime.now()
        time=(endtime-starttime).total_seconds()*1000
        if(os.path.exists('input.txt')):
            print("Time:",time,"ms")  
        
                    
    class FastReader(io.IOBase):
        newlines = 0
    
    def __init__(self, fd, chunk_size=1024 * 8):
            self._fd = fd
            self._chunk_size = chunk_size
            self.buffer = io.BytesIO()
    
    def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, self._chunk_size))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()
    
    def readline(self, size=-1):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, self._chunk_size if size == -1 else size))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()
    
    
    class FastWriter(io.IOBase):
    
    def __init__(self, fd):
            self._fd = fd
            self.buffer = io.BytesIO()
            self.write = self.buffer.write
    
    def flush(self):
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
    
    
    class FastStdin(io.IOBase):
    def __init__(self, fd=0):
            self.buffer = FastReader(fd)
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    
    
    class FastStdout(io.IOBase):
    def __init__(self, fd=1):
            self.buffer = FastWriter(fd)
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.flush = self.buffer.flush
    
    
    if __name__ == '__main__':
        sys.stdin = FastStdin()
        sys.stdout = FastStdout()
        main()
        