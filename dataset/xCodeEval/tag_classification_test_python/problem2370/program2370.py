def juli(s,i,a,c,t,g):
        od1 = min(abs(ord(s[i])%26 - a), 26 - abs(ord(s[i])%26 - a))
        od2 = min(abs(ord(s[i+1])%26 - c), 26 - abs(ord(s[i+1])%26 - c))
        od3 = min(abs(ord(s[i+2])%26 - t), 26 - abs(ord(s[i+2])%26 - t))
        od4 = min(abs(ord(s[i+3])%26 - g), 26 - abs(ord(s[i+3])%26 - g))
        return od1 + od2 + od3 + od4
    
    n = int(input(''))
    s = list(input(''))
    a = ord('A') % 26
    c = ord('C') % 26
    t = ord('T') % 26
    g = ord('G') % 26
    sumi = 100
    for i in range(len(s)-3):
        jl = juli(s,i,a,c,t,g)
        if jl < sumi:
            sumi = jl
    print(sumi)