def total_length(n):
        if n == 0 or n == 1: return 1
        return 2 * total_length(n / 2) + 1
    
def count_ones(n, pos, l, a, b):
        if pos - l > b or pos + l < a: return 0
        if n == 0: return 0
        if n == 1: return 1 if a <= pos <= b else 0
        return count_ones(n / 2, pos - l / 2, l / 2 + 1, a, b) \
             + (1 if a <= pos <= b and n % 2 == 1 else 0) \
             + count_ones(n / 2, pos + l / 2, l / 2 + 1, a, b)
    
    n, a, b = map(int, input().split())
    
    l = total_length(n)
    print(count_ones(n,) l / 2, l / 2 + 1, a - 1, b - 1)