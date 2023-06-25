def program1086():
    n = int(input())
    s = sorted([int(i)for i in input().split()])
    NON = []
    for i in range(n):
        if s[i] in NON:
            while s[i] in NON and s[i] > 0:
                s[i] -= 1
            NON.append(s[i])
        else:
            NON.append(s[i])
    print(sum(s))