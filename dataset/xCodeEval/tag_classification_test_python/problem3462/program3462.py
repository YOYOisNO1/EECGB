def program3462():
    n,st = int(input()), input()
    a = ['ogo']
    for i in range(100):
        a.append(a[0] + 'go'*(i+1))
    
    ans,flag = '',0
    for i in range(n):
        if i < flag:
            continue
        if st[i] != 'o':
            ans += st[i]
            continue
        curr = 'o'
        pos = i
        for j in range(i+1,n,2):
            if st[j:j+2] == 'go':
                pos = j+2
            else:
                break
        if pos > i:
            ans += '***'
            flag = pos
        else:
            ans += st[i]
    
    print(ans)