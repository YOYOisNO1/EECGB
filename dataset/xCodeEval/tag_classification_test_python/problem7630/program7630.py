def program7630():
    s = input()
    mod = int(input())
    s = s[::-1]
    tens = [1]
    for i in range(1, len(s)):
        tens.append(tens[i - 1] * 10 % mod)
    res = 0
    for i in range(0, len(s)):
        res += ((ord(s[i]) - ord('0')) * tens[i]) % mod
        res %= mod
    minc = res
    for i in range(0, len(s)):
        res -= ((ord(s[len(s) - 1 - i]) - ord('0')) * tens[len(s) - 1]) % mod
        res += mod
        res %= mod
        res *= 10
        res %= mod
        res += ord(s[len(s) - 1 - i]) - ord('0')
        res %= mod
        pos = len(s) - 2 - i
        if (pos < 0):
            pos += len(s)
        if (s[pos] != '0'):
            minc = min(minc, res)
    print(minc)