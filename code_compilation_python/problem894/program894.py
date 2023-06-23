def program894():
    n = int(input())
    s = input()
    cnt = 0
    bayan = set()
    for i in range(n):
        for j in range(n):
            if s[i] == s[j] and s[i] not in bayan and len(set(s[i:j])) == 2:
                cnt += 1
                bayan.add(s[i])
    print(len(set(s)) * cnt)