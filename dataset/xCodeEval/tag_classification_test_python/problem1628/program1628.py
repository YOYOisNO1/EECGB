def program1628():
    s = input()
     
    p = set()
    for i in range(2**len(s)):
        r = ''
        for j in range(len(s)):
            if 2**j & i:
                r += s[j]
        if r and r == r[::-1]:
            p.add(r)
    print(max(p))