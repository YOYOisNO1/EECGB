    n = int(input())
    s = input()
    
    ans = 0
    
    cs = ""
    cp = 1
    
def get_digit(s, n):
        for i in range(len(s)):
            if int(s[i:]) < n and s[i] != '0':
                return int(s[i:]), s[:i]
        return 0, s[:-1]
    
    while s:
        d, s = get_digit(s, n)
        ans += d*cp
        cp *= n
    
    print(ans)