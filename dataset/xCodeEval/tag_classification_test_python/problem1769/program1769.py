    s = input()
    t = input()
    
    
def check(sw):
        p = 0
        for i in sw:
            if i == t[p]:
                p += 1
            if p == len(t):
                break
        if p == len(t):
            return 1
        else:
            return 0
    
    
    op = 0
    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            o = s[0:i] + s[j + 1:len(s) + 1]
            if check(o):
                op = max(op, len(s) - len(o))
    
    print(op)