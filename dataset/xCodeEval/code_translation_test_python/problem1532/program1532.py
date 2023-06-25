    DIGITS = 55
    MAX_CNT = 6
    NUMBERS = [0] * (DIGITS + 1)
    CUTOFFS = [0] * (DIGITS + 1)
    
    for d in range(1, DIGITS + 1):
        NUMBERS[d] = 10 * NUMBERS[d - 1] + 1
        CUTOFFS[d] = 10**(d - 1) * 50 // 81 + 15
    
    INF = 10**9
    save = [{} for d in range(DIGITS)]
    
def recurse(value, d):
        if d == 0:
            return 0 if value == 0 else INF
    
        if value in save[d]:
            return save[d][value]
    
        ans = INF
    
        for cnt in range(0, MAX_CNT + 1):
            nvalue = abs(value - cnt * NUMBERS[d])
    
            if nvalue <= CUTOFFS[d]:
                ans = min(ans, cnt * d + recurse(nvalue, d - 1))
    
        save[d][value] = ans
        return ans
    
    X = int(input())
    print(recurse(X, len(str(X)) + 1))