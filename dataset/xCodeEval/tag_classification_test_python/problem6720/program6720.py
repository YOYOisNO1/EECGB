    DIGITS = 55
    MAX_CNT = 6
    CUTOFF_RATIO = 0.618
    NUMBERS = [0] * (DIGITS + 1)
    CUTOFFS = [0] * (DIGITS + 1)
    
    for d in range(1, DIGITS + 1):
        NUMBERS[d] = 10 * NUMBERS[d - 1] + 1
        CUTOFFS[d] = CUTOFF_RATIO * 10**(d - 1) + 15
    
    X = int(input())
    N = int(len(str(X)))
    candidates = {X: 0}
    
    for d in range(N + 1, 0, -1):
        ncandidates = {}
    
    def insert(value, cost):
            if value not in ncandidates or cost < ncandidates[value]:
                ncandidates[value] = cost
    
        for value in candidates:
            cost = candidates[value]
    
            for cnt in range(MAX_CNT + 1):
                nvalue = abs(value - cnt * NUMBERS[d])
    
                if nvalue <= CUTOFFS[d]:
                    insert(nvalue, cost + cnt * d)
    
        candidates = ncandidates
    
    print(candidates[0])