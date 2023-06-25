def program3373():
    
     s, j, l = input(), -1, [-1]
    for c in s:
        while j != -1 and c != s[j]:
            j = l[j]
        j += 1
        l.append(j)
    le = l[-1]
    if l.count(le) < 2:
        le = l[le]
    print(s[:le] if le > 0 else "Just a legend")