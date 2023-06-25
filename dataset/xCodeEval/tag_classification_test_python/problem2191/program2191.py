def program2191():
    """935A - Fafa and his Company
    http://codeforces.com/problemset/problem/935/A
    
    """
    # Problem #    : 935A
    # Created on   : 2019.06.09
    
    n = int(input())
    ans = 0
    
    for i in range(1, (n // 2) + 1):
        if (n - i) % i == 0:
            ans = ans + 1
    
    print(ans)
    