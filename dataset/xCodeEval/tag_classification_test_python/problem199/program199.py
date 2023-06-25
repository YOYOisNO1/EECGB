def program199():
    line = input()
    num_links = sum((1 for c in line if c == '-'), 0)
    num_pearls = sum((1 for c in line if c == 'o'), 0)
    
    if num_pearls == 0 or num_links % num_pearls == 0:
        print('YES')
    else:
        print('NO')