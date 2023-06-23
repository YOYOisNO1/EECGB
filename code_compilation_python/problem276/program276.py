def program276():
    n = int(input())
    s = list(map(int, input()))
    s1 = s.copy()
    diff, idx = 0, -1
    min_diff = max(s)+1
    for i in range(n):
        for j in range(len(s) - n):
            if s[i] > s[n + j]:
                diff = s[i] - s[n+j]
                if diff <min_diff:
                    min_diff = diff
                    idx = n+j
        if idx!=-1:
            s1.pop(idx)
            min_diff = max(s)+1
            idx = -1
        else:
            break
    diff, idx = 0, -1
    min_diff = max(s)+1
    for i in range(n):
        for j in range(len(s1) - n):
            if s1[i] < s1[n + j]:
                diff = s1[n+j] - s1[i]
                if diff < min_diff:
                    min_diff = diff
                    idx = n + j
        if idx!=-1:
            s1.pop(idx)
            min_diff = max(s1)+1
            idx = -1
        else:
            break
    
    if len(s) == n or len(s1) == n:
        print('YES')
    else:
        print('NO')