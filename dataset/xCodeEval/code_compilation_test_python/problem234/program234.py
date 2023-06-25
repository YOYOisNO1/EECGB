    s = input().strip()
    
    
def solve(s: str) -> int:
        n = len(s)
        pw = 2**n
        count = 0
        for mask in range(pw):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(s[i])
            if len(subset) == 3 and subset == ['Q', 'A', 'Q']:
                count += 1
    
        return count
    
    
    print(solve(s))