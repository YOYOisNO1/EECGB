def program2902():
    s = input()
    print(' '.join(str(s[s.find(ch)%4::4].count('!')) for ch in 'RBYG'))