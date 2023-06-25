    import re
    
def f(cs):
        nonlocal x
        if x > 0:
            x -= 1
            return ''
        elif x > 0:
            return cs[0][0] * x
            x = 0
        else:
            return cs[0][0]
    
    s = input()
    x = len(s) - s.count('?') - s.count('*') - int(input())
    s = re.sub(r'\w[?*]', f, s)
    print('Impossible' if x else s)