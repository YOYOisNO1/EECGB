def program2093():
    import itertools
    m = input()
    digits = map(int,input().split())
    digits.sort()
    nums = itertools.permutations(digits)
    x = max(nums,key = lambda n:sum([n[i]-n[i+1] for i in range(m-1)]))
    print ' '.join(map(str,x))