def solve(s, k):
        s = [ord(x) - ord('a') + 1 for x in sorted(set(s))]
        n = len(s)
    
        if n < k:
            return -1
    
        min_so_far = float('inf')
        for comb in combinations(s, k, -1, []):
            min_so_far = min(min_so_far, comb)
    
        if min_so_far == float('inf'):
            return -1
        return min_so_far
    
    
def combinations(s, k, idx, current):
        if len(current) == k:
            total = sum(current)
            # yield total, current
            yield total
        else:
            for i in range(idx + 1, len(s)):
                if len(current) and s[i] - current[-1] < 2:
                    continue
    
                current.append(s[i])
                yield from combinations(s, k, i, current)
                current.pop()  # Backtrack
    
    
def main():
        n, k = [int(x) for x in input().strip().split()]
        s = input().strip()
        print(solve(s, k))
    
    
    if __name__ == '__main__':
        main()