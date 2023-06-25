    import sys
    input=sys.stdin.readline
    
    from collections import defaultdict,deque
    from bisect import bisect_left,bisect_right
    from heapq import heappush,heappop
    from functools import lru_cache
    import math
    
def lcm(x, y):
        return int(x * y / gcd(x, y))
     
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
     
    # for _ in range(int(input())):
    #     x,y = list(map(int,input().split(' ')))
    #     if x == y == 0:
    #         print('0')
    #     else:
    #         s = math.sqrt(x**2+y**2)
    #         if int(s) == s:
    #             print('1')
    #         else:
    #             print('2')
     
    # for _ in range(int(input())):
    #     n,b,x,y = list(map(int,input().split(' ')))
    #     ans = 0
    #     i = 0
    #     t = 0
    #     while i < n:
    #         if t+x <= b:
    #             t += x
    #         else:
    #             t -= y
    #         ans += t
    #         i += 1
    #     print(ans)
     
    # for _ in range(int(input())):
    #     n = int(input())
    #     s = input()
    #     c = 0
    #     r = -1    
    #     i = 0
    #     cntl = cntr = 0
    #     f = ''
    #     ok = True
    #     ok1 = True
    #     while i < n:
    #         if ok:
    #             ok = False
    #             ok1 = True
    #             f = s[i]
    #             cntl = cntr = 0
    #             if s[i] == '(':
    #                 cntl += 1
    #             else:
    #                 cntr += 1
    #                 ok1 = False
    #         else:
    #             if s[i] == '(':
    #                 cntl += 1
    #             else:
    #                 cntr += 1
    #             if cntr > cntl:
    #                 ok1 = False
    #             if (ok1 and cntl == cntr) or s[i] == f:
    #                 ok = True
    #                 c += 1
    #                 r = i
    #         i += 1
    #     print(c,n-r-1)
    
    # n,C = list(map(int,input().split(' ')))
    # g = [0]*(C+1)
    # for _ in range(n):
    #     c,d,h = list(map(int,input().split(' ')))
    #     g[c] = max(g[c],d*h)
    # for c in range(1,C+1):
    #     g[c] = max(g[c],g[c-1])
    #     r = C//c
    #     for i in range(2,r+1):
    #         g[i*c] = max(g[i*c],i*g[c])
    # m = int(input())
    # for _ in range(m):
    #     D,H = list(map(int,input().split(' ')))
    #     t = bisect_left(g,D*H+1)
    #     if t == len(g):
    #         print(-1)
    #     else:
    #         print(t)
    
    n,k = list(map(int,input().split(' ')))
    N = 255
    mod = 998244353
    inv = [0]
    fac = [1]*(N+1)
    invfac = [1]*(N+1)
    for i in range(1,N+1):
        fac[i] = fac[i-1]*i%mod
    invfac[N] = pow(fac[N],mod-2,mod)
    for i in range(N)[::-1]:
        invfac[i] = invfac[i+1]*(i+1)%mod
    c =  [[1]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,i):
            c[i][j] = c[i-1][j] + c[i-1][j-1]
    p = [[1]*(N+1)**2 for _ in range(N+1)]
    for i in range((N+1)):
        for j in range(1,(N+1)**2):
            p[i][j] = p[i][j-1]*i%mod
    
    # @lru_cache(None)
# def C(i,j):
    #     if j == 0 or j == i:
    #         return 1
    #     return C(i-1,j)+C(i-1,j-1)
        # return fac[i]*invfac[j]*invfac[i-j]%mod
    # @lru_cache(None)
# def p(i,j):
    #     if j == 0:
    #         return 1
    #     return p(i,j-1)*i%mod
    dp = [[0]*(k+1) for _ in range(n+1)]
    s = [[0]*(k+1) for _ in range(n+1)]
    dp[1][0] = s[1][0] = 1
    for j in range(1,k+1):
        dp[2][j] = 1
        s[1][j] = s[1][j-1] + dp[1][j]
        s[2][j] = s[2][j-1] + dp[2][j]
    for i in range(3,n+1):
        for j in range(1,k+1):
            for z in range(1,i):
                dp[i][j] += s[i-z][j-1]*c[i-1][z]*p[k+1-j][z*(z-1)//2+z*(i-1-z)]%mod  
            s[i][j] = (s[i][j-1] + dp[i][j]) % mod
    print(s[n][k])
    
        
    
    
    
    