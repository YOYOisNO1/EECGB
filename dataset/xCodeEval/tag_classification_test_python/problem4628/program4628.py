    import sys
    
def solve(n, k, letters):
        start_positions = {}
        end_positions = {}
        for idx, letter in enumerate(letters):
            if letter not in start_positions:
                start_positions[letter] = idx
                end_positions[letter] = idx + 1
            else:
                end_positions[letter] = idx + 1
    
        inv_end_positions = {}
        inv_start_positions = {}
        for position in start_positions:
            if start_positions[position] in inv_start_positions:
                inv_start_positions[start_positions[position]] += 1
            else:
                inv_start_positions[start_positions[position]] = 1
    
        for position in end_positions:
            if end_positions[position] in inv_end_positions:
                inv_end_positions[end_positions[position]] += 1
            else:
                inv_end_positions[end_positions[position]] = 1
    
        num_open = 0
        for l in range(10**6+1):
            if l in inv_end_positions:
                num_open -= inv_end_positions[l]
            if l in inv_start_positions:
                num_open += inv_start_positions[l]
            if num_open > k:
                return "YES"
    
        return "NO"
    
    if __name__ == "__main__":
        n, k = map(int, sys.stdin.readline().split())
        letters = list(sys.stdin.readline().strip())
        print(solve(n,) k, letters)