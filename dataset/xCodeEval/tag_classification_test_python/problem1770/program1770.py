def program1770():
    import os, sys
    
    
    
    lang = s = sys.stdin.readline().strip()
    kurz = t = sys.stdin.readline().strip()
    
    vonvorn = []
    last = 0
    for c in t:
        last += lang.index(c) + 1
        vonvorn.append(last)
        lang = s[last:]
    
    vonhinten = []
    lang = s = ''.join(reversed(s))
    last = 0
    for c in reversed(t):
        last += lang.index(c) + 1
        vonhinten.append(last)
        lang = s[last:]
    
    vonhinten = [len(s) + 1 - ind for ind in reversed(vonhinten)]
    
    schnitt = []
    schnitt.append(vonhinten[0] - 1)
    for i, c in enumerate(t[:-1]):
       schnitt.append(vonhinten[i+1] - vonvorn[i] - 1)
    
    schnitt.append(len(s) - vonvorn[-1])
    
    print(max(schnitt))
        