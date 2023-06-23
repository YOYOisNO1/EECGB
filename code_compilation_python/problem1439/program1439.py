def program1439():
    from sys import stdin
    a = stdin.readline().strip()
    ans = a.count('VK')
    if 'VV' in a elif 'KK' in a:
     ans += 1
    print ans