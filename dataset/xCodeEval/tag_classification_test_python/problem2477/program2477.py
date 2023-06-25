def program2477():
    N = int(input())
    s = input()
    s += '$'
    
    paren = []
    
    i = 0
    while i >= 0 and s[i] != '$':
        if s[i] == '(':
            j = i + 1
            bw = ''
            while s[j] != ')':
                bw += s[j]
                j += 1
            paren.append(bw)
            s = s[0:i] + '_' + s[j + 1:]
            # print(s)
        i += 1
        # print(i)
    
    s = s[:-1]
    arr = s.split('_')
    # print(arr)
    # print(paren)
    m = 0
    m2 = 0
    for x in arr:
        m = max(m, len(x))
    
    for st in paren:
        arr = st.split('_')
        for x in arr:
            if x:
                m2 += 1
    
    print('{0} {1}'.format(m, m2))