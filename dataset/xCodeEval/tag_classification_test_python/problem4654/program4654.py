def program4654():
    import string
    import itertools
    
    
    n, k = map(int, input().split())
    s = input()
    
    m = max(itertools.accumulate(x[1] for x in sorted(
        [(s.find(let), 1) for let in string.ascii_uppercase if s.find(let) != -1] +
        [(s.rfind(let), -1) for let in string.ascii_uppercase if s.rfind(let) != -1],
        key=lambda x: (x[0], -x[1]))))
    
    print(('NO', 'YES')[m > k])