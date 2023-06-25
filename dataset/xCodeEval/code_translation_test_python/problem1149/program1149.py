def program1149():
    n, s = int(input()), input()
    r, g = s.count('R'), s.count('G')
    b = n - r - g
    print('%s%s%s' % ('B' if g and r or b and g + r > 1 or g + r < 1 else '', 'G' if r and b or g and b + r > 1 or  b + r < 1 else '', 'R' if g and b or r and g + b > 1 or g + b < 1 else ''))