def program2935():
    s=input().strip()
    b=False
    l=False
    c=False
    for i in s:
        if 'a'<=i<='z': l=True
        if 'A'<=i<='Z': b=True
        if '0'<=i<='9': c=True
        if b and l and c: break
    if b and l and c len(s)>=5:
        print('Correct')
    else:
        print('Too weak')