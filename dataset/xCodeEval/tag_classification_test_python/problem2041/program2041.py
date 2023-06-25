    
    
def read_int():
        return int(input().strip())
    
    
def read_ints():
        return list(map(int, input().strip().split(' ')))
    
    
def solve():
        """
        OPT[sum of edges][has at least >= d]
        OPT[i][false] = sum(OPT[i-j][false]) j=1..d-1
        OPT[i][true] = OPT[i-j][false] j>=d
                       OPT[i-j][true]  j=1..k
        """
        n, k, d = read_ints()
        modulo = 10**9+7
        OPT = [
            [0, 0] for _ in range(n+1)
        ]
        OPT[0][False] = 1
        for i in range(1, n+1):
            OPT[i][False] = sum(OPT[i-j][False] for j in range(1, min(i+1, d)))%modulo
            OPT[i][True] = (sum(OPT[i-j][False] for j in range(d, min(i+1, k+1)))+
                            sum(OPT[i-j][True] for j in range(1, min(i+1, k+1))))%modulo
        return OPT[-1][True]
    
    
    if __name__ == '__main__':
        print(solve())