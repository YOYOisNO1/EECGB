def program2437():
    N = int(input())
    S = input()
    a,b = (0,0)
    cur,inside = (0,0)
    for c in S:
        if c == '(':
            inside = 1
            cur = 0
        elif c == ')':
            inside = 0
            if cur: b+=1
            cur = 0
        elif c == '_':
            if inside and cur: b+=1
            cur = 0
        else:
            cur+=1
            if not inside: a = max(a,cur)
    print(a,b)