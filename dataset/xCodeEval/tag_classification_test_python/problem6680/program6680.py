    #
    # http://codeforces.com/problemset/problem/655/A
    import sys
    
    
def normalize(s):
        s = s.replace('X', '')
        i = s.index('A')
        return s[i] + s[(i + 1) % 3] + s[(i + 2) % 3]
    
    
def read_line():
        return next(sys.stdin).strip()
    
    
    a = normalize(read_line() + read_line()[::-1])
    b = normalize(read_line() + read_line()[::-1])
    
    print('YES') if a == b else 'NO'