def program764():
    n = int(input())
    #n, m = map(int, input().split())
    s = input()
    #c = list(map(int, input().split()))
    k = s[:n // 2].count('4') * 4 + s[:n // 2].count('7') * 7
    l = s[n // 2:].count('4') * 4 + s[n // 2:].count('7') * 7
    if (n % 2 == 0 and s.count('4') + s.count('7') == n and 
        k == l):
        print('YES')
    else:
        print('NO')
                                    