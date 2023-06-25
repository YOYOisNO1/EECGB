def program2469():
    import string
    input()
    s=input()
    a, b=0, 0
    while s.find('(')>=0:
        l, r=s.find('('), s.find(')')
        a=max(a, *map(len, s[:l].split('_')))
        b+=sum(1 for t in s[l+1:r].split('_') if t!='')
        s=s[r+1:]
    a=max(a, *map(len, s.split('_')))
    print(a, b)