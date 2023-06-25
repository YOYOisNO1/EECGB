    # import tensorflow as tf
    import math
    from itertools import product
    
    
def formula(counts):
        ans = math.factorial(sum(counts))
        for c in counts:
            ans /= math.factorial(c)
        if counts[0]:
            ans = (ans * (sum(counts) - counts[0])) / sum(counts)
        return ans
    
    
def solve(n):
        s = str(n)
        counts = [s.count(str(i)) for i in range(10)]
        ans = 0
        possible_counts = [range(1, c + 1) if c != 0 else [0] for c in counts]
        results = [formula(counts) for counts in product(*possible_counts)]
        ans = sum(results)
        #  print(list(product(*possible_counts)))
        #  print(results)
        #  print(ans)
        return ans
    
    
def test():
        assert solve(97) == 2
        assert solve(2028) == 13
    
    
    if __name__ == '__main__':
        test()
        n = int(input())
        print(solve(n))