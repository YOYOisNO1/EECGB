def program1570():
    n, p, k = map(int, input().split())
    
    ans = [i for i in range(p - k, p + k + 1)]
    
    while ans[0] < 1:
        ans.pop(0)
    while ans[-1] > n:
        ans.pop()
    
    if ans[0] > 1:
        ans = ['<<'] + ans
    if ans[-1] < n:
        ans.append('>>')
    for i in range(len(ans)):
        if ans[i] == p:
            ans[i] = f'({p})'
    print(*ans)