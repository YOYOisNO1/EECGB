def program239():
    n = int(input())
    s = input()
    count = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if (s[i] == s[j]):
                count += 1
                j += 1
        i = j
    print(count)