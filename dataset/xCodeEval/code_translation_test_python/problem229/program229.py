    s = map(int, input().split())
    
def dooable(s):
        import itertools
        for p in itertools.permutations(s):
            if sum(p[:3]) == sum(p[3:]):
                return True
        return False
    print(["NO",) "YES"][dooable(s)]