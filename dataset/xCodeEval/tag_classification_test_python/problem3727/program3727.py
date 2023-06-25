    from bisect import bisect_left, bisect_right
    
    
def read_ints():
        return map(int, input().split())
    
    
    n, d = read_ints()
    x_seq = sorted(read_ints())
    
    # N * log(N) is enough
    max_n_can_remain = max(
        bisect_right(x_seq, begin+d) - bisect_left(x_seq, begin)
        for begin in x_seq
    )
    
    print(n - max_n_can_remain)