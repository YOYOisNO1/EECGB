def program4506():
    n, m, k, r, c = map(int, input().split())
    ax, ay, bx, by = map(int, input().split())
    print(pow(k, n*m - (r*c if (ax,ay) != (bx,by) else 0), 10**9+7))