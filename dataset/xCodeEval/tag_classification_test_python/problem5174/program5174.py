    import sys
    
    sys.setrecursionlimit(10000)
    
def count_ones(n, limit_left, limit_right):
    def tree_nodes(n):
            if n == 0:
                return 1
            return 2 ** n.bit_length() - 1
    
    def f(n, start):
            if start > limit_right:
                return 0
    
            nodes = tree_nodes(n)
            if start + nodes <= limit_left:
                return 0
    
            if n <= 1:
                return n
    
            subtree_nodes = (nodes - 1) // 2
    
            result = f(n // 2, start) + f(n // 2, start + subtree_nodes + 1)
    
            if limit_left <= start + subtree_nodes <= limit_right:
                result += 1 if n % 2 == 1 else 0
    
            return result
    
        return f(n, 0)
    
    n, left, right = map(int, sys.stdin.readline().split(' '))
    print(count_ones(n, left - 1, right - 1))