    """
    Codeforces Round #334 (Div. 2)
    
    Problem 846 A. Curriculum Vitae
    
    @author yamaton
    @date 2017-09-13
    """
    
    
def count(xs, i):
        return xs[:i].count(0) + xs[i:].count(1)
    
    
def solve(xs):
        n = len(xs)
        return max(count(xs, i) for i in range(n + 1))
    
    
def main():
        n = int(input())
        xs = [int(c) for c in input().split()]
        assert len(xs) == n
        result = solve(xs)
        print(result)
    
    
    if __name__ == '__main__':
        main()