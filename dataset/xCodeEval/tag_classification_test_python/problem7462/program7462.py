def program7462():
    F = lambda x : x * F(x - 1) if x else 1
    r = [1, 3, 15, 133, 2025, 37851, 1030367, 36362925]
    n = input()						
    print(r[n) / 2] * F(n) % 1000000007 if n & 1 else 0