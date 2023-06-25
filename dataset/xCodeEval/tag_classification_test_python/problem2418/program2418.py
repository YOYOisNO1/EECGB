def program2418():
    input()
    l = input().replace(')', '(').split('(')
    print(max(len(w) for s in l[::2] for w in s.split('_')),
          len([w for s in l[1::2] for w in s.split('_') if w]))