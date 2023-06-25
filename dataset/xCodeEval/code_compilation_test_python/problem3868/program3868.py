def program3868():
    s = input()
    s_len = len(s)
    ans = {'R' : 0, 'B' : 0, 'Y' : 0, 'G' : 0}
    for i in range(s_len):
        if s[i] == '!':
            j = i
            k = i
            if i <= 3:
                while s[j] == '!' :
                    j += 4
                ans[s[j]] += 1
            elif s_len - i <= 3:
                while s[k] == '!':
                    k -= 4
                ans[s[k]] += 1
            else :
                while s[j] == '!' and s[k] == '!':
                if len_n - j <= 3:
                    j = i
                if k <= 3:
                    k = i
                    j += 4
                    k -= 4
                if s[j] == '!':
                    ans[s[k]] += 1
                else :
                    ans[s[j]] += 1
    result = ' '.join(str(value) for value in ans.values())
    print(result)