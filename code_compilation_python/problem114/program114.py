def program114():
    s = input()
    
    v = ['A','E','I','O','U','Y']
    n = 0
    a = -1
    for i in xrange(len(s)):
        if s[i] in v:
            if i-a>n:
                n = i-a
            a = i
    print n if n>0 else len(s)+1