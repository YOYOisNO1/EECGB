    '''
    686
    479 178 29
    11 145 530
    '''
    import sys
    
    
def input():
        return sys.stdin.readline()
    
    n = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    
    
    
    
    total_parties = sum(a)
    
def max_wins(a, b):
        a = list(a)
        b = list(b)
        res = 0
        for i in range(-1, len(a)-1):
            wins = min(a[i], b[i+1])
    
            res += wins
            a[i] -= wins
            b[i+1] -= wins
    
        return res
    
def max_not_wins(a, b):
        a = list(a)
        b = list(b)
    
    
        _max_res = 0
        res = 0
    
        pairs = [
            (0, -1),
            (1, 0),
            (2, 1),
            (0, 0),
            (1, 1),
            (2, 2),
        ]
    
    def permutations(seq):
            if len(seq) == 1:
                return [seq]
    
            else:
                res = []
                for i in range(len(seq)):
                    for perm in permutations(seq[:i]+ seq[i+1:]):
                        new = [seq[i]] + perm
                        res.append(new)
                
                return res
    
    def get_max(perm, a, b):
            a = list(a)
            b = list(b)
            res = 0
            for i,j in perm:
                not_wins = min(a[i], b[j])
                a[i] -= not_wins
                b[j] -= not_wins
                res += not_wins
    
            return res
    
        for perm in permutations(pairs):
            _max_res = max(_max_res, get_max(perm, a, b))
    
        return _max_res
    
    print(sum(a) - max_not_wins(a, b), max_wins(a, b))