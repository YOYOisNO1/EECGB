    from itertools import combinations
    
def solve(s, k):
        s = [ord(x) - ord('a') + 1 for x in list(sorted(set(s)))]
        n = len(s)
    
        if n < k:
            return -1
    
        min_so_far = float('inf'), None
        for comb in combinations(s, k):
            if any([j - i < 2 for (i, j) in zip(comb[:-1], comb[1:])]):
                continue
            tmp = sum(comb)
            if tmp < min_so_far[0]:
                min_so_far = tmp, comb
    
        if min_so_far[1] is not None:
            return min_so_far[0]
        return -1 
    
    
def main():
        n, k = [int(x) for x in input().strip().split()]
        s = input().strip()
        print(solve(s, k))
    
    
    if __name__ == '__main__':
        main()