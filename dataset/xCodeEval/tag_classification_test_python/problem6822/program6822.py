def program6822():
    from collections import Counter
    k = int(input())
    alph = 'abcdefghijklmnopqrstuvwxyz'[:k]
    s = input()
    n = len(s)
    new_s = []
    for i in range(n):
        c1 = s[i]
        c2 = s[n-1-i]
        if c1!=c2 and "?" not in (c1, c2):
            new_s = "IMPOSSIBLE"
            break
        elif c1 == "?":
            new_s.append(c2)
        else:
            new_s.append(c1)
    other_alph = ''
    for a in alph:
        if a not in new_s:
            other_alph = a + other_alph
    cur_count = len(alph) - len(other_alph)
    vars_count = new_s.count("?")//2 + new_s.count("?")%2
    else_count = sum([1 if c not in alph+"?" else 0 for c in new_s])
    if new_s=="IMPOSSIBLE" or cur_count+vars_count < k or else_count>0:
        print("IMPOSSIBLE")
    else:
        for i in range(len(new_s)):
            c = new_s[i]
            if c == "?":
                if cur_count+vars_count>k:
                    c = 'a'
                else:
                    c = other_alph[vars_count-1]
                new_s[n-1-i] = c
                vars_count-=1                
            print(c, end="")