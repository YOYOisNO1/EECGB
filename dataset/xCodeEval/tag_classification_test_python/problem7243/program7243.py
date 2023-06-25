def program7243():
    # https://codeforces.com/problemset/problem/452/C
    n, m = map(int, input().split())
    
    if n*m==1:
        print(1)
    else:
        print(1/n  + (m-1)*(n-1) / ((m*n-1) * n))