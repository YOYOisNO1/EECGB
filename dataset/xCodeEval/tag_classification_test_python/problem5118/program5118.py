def calc_len(n):
        result = 0
        pow = 0
        while (n // 2):
           pow += 1
           n //= 2
        result += 1 << (pow + 1 )
        return result - 1
    
def calc_1(n, l, r, len):
        if n == 1:
            return 1
        if n == 0:
            return 0
        result = 0
        if l <= (len//2 + 1) and r >= (len//2 + 1) and n % 2:
            result = 1
        if l <= len//2:
            result += calc_1(n//2, l, min(r, len//2), len // 2 )
        if r >= len//2 + 2:
            result += calc_1(n//2, max (1, l - (len//2 + 1) ), r - (len // 2 + 1), len // 2)
        return result
    
    line = input().split()
    n = int(line[0])
    l = int(line[1])
    r = int(line[2])
    len = calc_len(n)
    print(calc_1(n,l, r, len))
    