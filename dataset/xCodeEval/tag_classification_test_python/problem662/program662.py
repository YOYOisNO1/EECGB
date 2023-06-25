def program662():
    s = input()
    cnt = jump = 0
    vowels = ['A','E','I','O','U','Y']
    for i in range(len(s)):
        if s[i] not in vowels:
            cnt += 1
            if cnt > jump:
                jump = cnt
        else:
            cnt = 0
    print(jump+1)