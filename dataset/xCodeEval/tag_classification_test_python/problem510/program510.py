def program510():
    n, k = list (map (int, input ().split ()))
    s = input()
    
    sett = {s}
    q = [s]
    
    m = n
    
    while len (q) and len (sett) < k:
        node = q.pop (0)
        for i in range (0, len (node)) :
            ss = node[:i] + node[i + 1:]
            if not ss in sett and len (sett) < k :
                q.append(ss)
                sett.add(ss)
                m += len (ss)
    
    print(('-1') if len (sett) < k else n * k - m)