    import sys
    import os
    
def cycle_len(graph, start, visited):
        res = 1
        i = graph[start]
        while i != start:
            visited[i] = True
            i = graph[i]
            res += 1
        return res
    
def gcd2(a, b):
        while a != 0:
            if a > b:
                a, b = b, a
            else:
                a, b = b % a, a
        return b
    
def gcd(nums):
        return reduce(gcd2, nums, 0)
    
def mult(a, b):
        return a * b
    
def lcm(nums):
        return reduce(mult, nums, 1) // gcd(nums)
    
    
def lcm2(nums):
        if len(nums) == 1:
            return nums[0]
        temp = lcm2(nums[1:])
        return (nums[0] * temp) // gcd2(nums[0], temp)
    
def can_partitioned_into_cycles(graph):
        in_degs = {}
        for u in xrange(len(graph)):
            v = graph[u]
            if v not in in_degs:
                in_degs[v] = 1
            else:
                in_degs[v] = in_degs[v] + 1
        for _, cnt in in_degs.iteritems():
            if cnt != 1:
                return False
        return True
    
def solve(graph):
        if not can_partitioned_into_cycles(graph):
            return -1
        factors = set()
        visited = [False for _ in xrange(len(graph))]
        for i in xrange(len(graph)):
            if visited[i]:
                continue
            cycle = cycle_len(graph, i, visited)
            factor = cycle // 2 if cycle % 2 == 0 else cycle
            factors.add(factor)
        return lcm2(list(factors))
    
def read_input():
        ints = map(int, sys.stdin.read().split())
        return map(lambda n: n - 1, ints[1:])
    
    print(solve(read_input()))
    