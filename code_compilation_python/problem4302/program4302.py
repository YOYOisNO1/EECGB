    #!/usr/bin/env python
    from __future__ import division, print_function
     
    import os
    import sys
    from io import BytesIO, IOBase
     
    if sys.version_info[0] < 3:
        from __builtin__ import xrange as range
        from future_builtins import ascii, filter, hex, map, oct
     
    import __pypy__
     
    add = __pypy__.intop.int_add
    sub = __pypy__.intop.int_sub
    mul = __pypy__.intop.int_mul
     
     
    import random
    import collections
    import math
    import itertools
    import bisect
     
    class MinQueue:
    def __init__(self):
            self.q = collections.deque()
            self.minq = collections.deque()
     
    def offer(self, x):
            self.q.append(x)
            while self.minq and self.minq[-1] > x:
                self.minq.pop()
            self.minq.append(x)
     
    def poll(self):
            if self.minq[0] == self.q.popleft():
                self.minq.popleft()
     
    def min(self):
            return self.minq[0]
     
     
def real_main():
        n, m, a, b = read_int_array()
        g0, x, y, z = read_int_array()
        
        zinv = 1.0/z
        
    def modmuladd(x,y,c):
            ans = sub(add(mul(x,y),c), mul(z, int(zinv*x*y + zinv*c)))
            if ans >= z:
                return ans - z
            elif ans < 0:
                return ans + z
            else:
                return ans
     
        prefix = []
        for r in range(n):
            row_mins = []
            q = MinQueue()
            for c in range(b):
                q.offer(g0)
                g0 = modmuladd(g0, x, y)
     
            row_mins.append(q.min())
            for c in range(b, m):
                q.poll()
                q.offer(g0)
                g0 = modmuladd(g0, x, y)
                row_mins.append(q.min())
            prefix.append(row_mins)
     
        prefix = zip(*prefix)
     
        ans = 0.0
        for c in range(len(prefix[0])):
            tmp = prefix[c]
            q = MinQueue()
            for i in range(a):
                q.offer(tmp[i])
            ans += q.min()
            for r in range(a, n):
                q.poll()
                q.offer(tmp[r])
                ans += q.min()
        print(int(ans))
     
     
def solve():
        pass
     
     
def main():
        if False and 'PYCHARM_HOSTED' in os.environ:
            main_pycharm()
        else:
            real_main()
     
     
    from copy import deepcopy
def main_pycharm():
        solution = solve
     
        test_inputs = None
        test_outputs = None
        judge = None
        slow_solution = None
        if solution is not None:
            if test_outputs is not None:
                test_with_answers(solution, test_inputs, test_outputs)
            if judge is not None:
                test_with_judge(solution, test_inputs, judge)
            if slow_solution is not None:
                test_with_slow_solution(solution, test_inputs, slow_solution)
     
     
def test_with_answers(solution, inputs, answers):
        total, wrong = 0, 0
        for args, test_ans in zip(inputs, answers):
            ans = solution(*deepcopy(args))
            if ans != test_ans:
                print('WRONG! ans=%s, test_ans=%s, args=%s' % (ans, test_ans, args))
                wrong += 1
            else:
                print('GOOD')
            total += 1
        print('ALL %d TESTS PASSED' % total if not wrong else '%d out of %d tests are WRONG' % (wrong, total))
     
     
def test_with_judge(solution, inputs_gen, judge):
        total, wrong = 0, 0
        for args in inputs_gen:
            ans = solution(*deepcopy(args))
            if not judge(deepcopy(ans), *deepcopy(args)):
                print('WRONG! ans=%s, args=%s' % (ans, args))
                wrong += 1
            total += 1
        print('ALL %d TESTS PASSED' % total if not wrong else '%d out of %d tests are WRONG' % (wrong, total))
     
     
def test_with_slow_solution(solution, inputs_gen, solution_slow):
        total, wrong = 0, 0
        for args in inputs_gen:
            ans = solution(*deepcopy(args))
            slow = solution_slow(*deepcopy(args))
            if ans != slow:
                print('WRONG! ans=%s, slow=%s, args=%s' % (ans, slow, args))
                wrong += 1
            total += 1
        print('ALL %d TESTS PASSED' % total if not wrong else '%d out of %d tests are WRONG' % (wrong, total))
     
def generate_nums(n, min, max, check_if_good=None):
        while True:
            nums = [random.randint(min, max) for _ in range(n)]
            if check_if_good is None or check_if_good(nums):
                return nums
     
    # This mergesort can be like 7 times faster than build in sort
    # (for stupid reasons)
def mergesort(A, key=lambda x: x, reverse=False):
        C = A
        A = list(range(len(A)))
        B = list(A)
     
        n = len(A)
        for i in range(0, n - 1, 2):
            if key(C[A[i]]) > key(C[A[i ^ 1]]):
                A[i], A[i ^ 1] = A[i ^ 1], A[i]
     
        width = 2
        while width < n:
            for i in range(0, n, 2 * width):
                R1, R2 = min(i + width, n), min(i + 2 * width, n)
                j, k = R1, i
                while i < R1 and j < R2:
                    if key(C[A[i]]) > key(C[A[j]]):
                        B[k] = A[j]
                        j += 1
                    else:
                        B[k] = A[i]
                        i += 1
                    k += 1
                while i < R1:
                    B[k] = A[i]
                    k += 1
                    i += 1
                while k < R2:
                    B[k] = A[k]
                    k += 1
            A, B = B, A
            width *= 2
     
        if reverse:
            A.reverse()
        return A
     
def mergesort_simple(A, reverse=False):
        C = A
        A = list(range(len(A)))
        B = list(A)
     
        n = len(A)
        for i in range(0, n - 1, 2):
            if C[A[i]] > C[A[i ^ 1]]:
                A[i], A[i ^ 1] = A[i ^ 1], A[i]
     
        width = 2
        while width < n:
            for i in range(0, n, 2 * width):
                R1, R2 = min(i + width, n), min(i + 2 * width, n)
                j, k = R1, i
                while i < R1 and j < R2:
                    if C[A[i]] > C[A[j]]:
                        B[k] = A[j]
                        j += 1
                    else:
                        B[k] = A[i]
                        i += 1
                    k += 1
                while i < R1:
                    B[k] = A[i]
                    k += 1
                    i += 1
                while k < R2:
                    B[k] = A[k]
                    k += 1
            A, B = B, A
            width *= 2
     
        if reverse:
            A.reverse()
        return A
     
     
    # region fastio
     
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
     
def read():
        return input()
     
def read_int():
        return int(input())
     
def read_array(sep=None, maxsplit=-1):
        return input().split(sep, maxsplit)
     
def read_int_array():
        return [int(a) for a in read_array()]
     
    # endregion
     
    if __name__ == "__main__":
        main()