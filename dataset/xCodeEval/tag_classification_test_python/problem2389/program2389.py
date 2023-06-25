def program2389():
    s = input()
    n = s.count('VK')
    s = s.replace('VK', '__')
    if 'VV' in s or 'KK' in s:
        n = n + 1
    print(n)