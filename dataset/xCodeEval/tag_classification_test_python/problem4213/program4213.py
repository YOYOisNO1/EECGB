def program4213():
    s = input()
    print(['NO',) 'YES'][any([s[:i] + s[j + 1:] == 'CODEFORCES' for i in range(len(s)) for j in range(i, len(s))])]