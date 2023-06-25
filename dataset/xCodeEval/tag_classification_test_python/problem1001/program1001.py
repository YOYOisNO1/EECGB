def program1001():
    from itertools import permutations
    n = int(input())
    ar, asis, apap = [int(i) for i in input().split()]
    br, bsis, bpap = [int(i) for i in input().split()]
    ma = min(ar, bsis) + min(asis, bpap) + min(apap, br)
    mi = max(ar - br - bpap, 0) + max(asis - bsis - br, 0) + max(apap - bpap - bsis, 0)
    print(mi, ma)