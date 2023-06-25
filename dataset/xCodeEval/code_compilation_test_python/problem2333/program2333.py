def program2333():
    st = list(input())
    for i in range(len(st)):
        if st[i] == '/':
            for j in range(i+1.n):
                if st[j] == '/':
                    st[j] = None
                else:
                    break
    
    print(''.join(lst))