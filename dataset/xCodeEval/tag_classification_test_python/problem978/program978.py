    import sys
    from itertools import permutations
    from copy import deepcopy
    
    
def solve(input_path=None):
        if input_path is None:
            f = sys.stdin
        else:
            f = open(input_path, 'r')
    
        n = int(f.readline())
        a = list(map(int, f.readline().split()))
        b = list(map(int, f.readline().split()))
    
        min_win = n
        cases = list()
        cases.append((0, 0))
        cases.append((0, 2))
        cases.append((1, 1))
        cases.append((1, 0))
        cases.append((2, 2))
        cases.append((2, 1))
        cases = sorted(cases)
    
        for case in permutations(cases):
            a_temp = deepcopy(a)
            b_temp = deepcopy(b)
    
            for match in case:
                cnt = min(a_temp[match[0]], b_temp[match[1]])
                a_temp[match[0]] -= cnt
                b_temp[match[1]] -= cnt
            cur = min(a_temp[0], b_temp[1]) + min(a_temp[1], b_temp[2]) + min(a_temp[2], b_temp[0])
    
            min_win = min(min_win, cur)
    
        max_win = min(a[0], b[1]) + min(a[1], b[2]) + min(a[2], b[0])
    
        return [f"{min_win} {max_win}"]
    
    
def main():
        for line in solve():
            print(f"{line}")
    
    
    if __name__ == '__main__':
        main()