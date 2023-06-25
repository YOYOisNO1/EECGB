def reverse(s):
        res = ''
        for i in range(n - 1):
            if s[i] == 'W': res += 'E'
            elif s[i] == 'E': res += 'W'
            elif s[i] == 'N': res += 'S'
            elif s[i] == 'S': res += 'N'
        return res
    n = int(input())
    s1 = input()
    s2 = input()
    s2 = reverse(s2)[::-1]
    f = 1
    for i in range(1, n):
        if s2[0:i] == s1[n - i - 1:n - 1]:
            f = 0
            break
        
    print ( 'YES' if f else 'NO')