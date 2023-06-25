def program4588():
    (n, k) = tuple(map(int, input().split(' ')))
    s = input()
    start = {}
    end = {}
    for i in range(n):
        if s[i] not in start:
            start[s[i]] = i
        if s[n-i-1] not in end:
            end[s[n-i-1]] = n-i-1
    
    current = 0
    ans = False
    for i in range(n):
        if i == start[s[i]]:
            current += 1
        if current > k:
            ans = True
            break
        if i == end[s[i]]:
            current -= 1
        if current > k:
            ans = True
            break
    if ans:
        print("YES")
    else:
        print("NO")