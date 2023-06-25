def program4281():
    input()
    w,s=set('aeiouy'),input()
    print(''.join(c[0] for c in zip(s,'b'+s) if not set(c)<w))