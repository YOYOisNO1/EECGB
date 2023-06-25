def is_aut(s, t):
        i = 0
        for c in s:
            if c == t[i]:
                i += 1
            if i == len(t):
                break
        
        return i == len(t)
    
    s = input()
    t = input()
    
    ss = str(sorted(s))
    st = str(sorted(t))
    
    if ss == st:
        print('array')
    elif is_aut(s, t):
        print('automaton')
    elif is_aut(ss, st):
        print('both')
    else:
        print('need tree')