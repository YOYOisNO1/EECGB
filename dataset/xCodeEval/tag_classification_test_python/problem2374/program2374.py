def program2374():
    N = int(input())
    S = list(map(lambda c: ord(c) - ord('A'), input()))
    
    TARGET = [0, ord('C') - ord('A'), ord('T') - ord('A'), ord('G') - ord('A')]
    
    MIN = 26 * 4 + 1
    for st in range(N - 3):
        cost = 0
        for ind in range(4):
            cost += min((S[st + ind] - TARGET[ind]) % 26, (TARGET[ind] - S[st + ind]) % 26)
        MIN = min(MIN, cost)
    
    print(MIN)