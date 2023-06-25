def program2959():
    s = input()
    if s.isupper() or (s[0].islower() and s[1:].isupper()) or len(s) == 1:
        s = ''.join(map(lambda x: x.lower() if x.isupper() else x.upper(), s))
    
    print(s)