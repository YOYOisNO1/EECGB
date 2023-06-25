def program4435():
    d = {'at':'@',
         'dot':'.'}
    s = input()
    n = len(s)
    i = 0 
    ss = ""
    ct = 0
    while i<n:
        s1 = s[i:i+2]
        s2 = s[i:i+3]
        if s1 in d and not(i==0) and not(i==(n-2)) and ct==0:
            ss+=d[s1]
            ct += 1
            i += 1
        elif s2 in d and not(i==0) and not(i==(n-2)) and not(i==(n-3)):
            ss+=d[s2]
            i+=2
        else:
            ss+=s[i]
        i+=1
    print(ss)