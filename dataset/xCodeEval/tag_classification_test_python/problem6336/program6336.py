def program6336():
    #!/usr/bin/env python3
    
    l, d = [], {}
    for i, c in enumerate(input()):
        if c in d:
            d1, len = d[c], (i-d[c]-1)//2 +1
            d2  = i
        else:
            l.append(c)
        d[c] = i
    s = ''.join(l*2)
    if d2-d1 <= 1:
        print("Impossible")
    else:
        print(s[d1+26-13+len:d1+26] + s[d1:d1+len] + '\n' + s[d1+len:d1+len+13][::-1])