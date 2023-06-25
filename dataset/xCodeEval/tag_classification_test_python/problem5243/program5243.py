def program5243():
    from itertools import *
    n,k = map(int, str(input()).split())
    s = [str(input()) for i in range(n)]
    final = 10**k
    for i in permutations(range(k)):
        x = [''.join([y[j] for j in i]) for y in s]
        final = min(int(max(x)) - int(min(x)), final)
    print(final)