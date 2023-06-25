def program2597():
    for _ in range(int(input())):
        h, w, k = map(int, input().split())
        if w%2:h, w = w, h;k = (h*w)//2-k
        k -= (h%2*w//2);print("NO" if k%2 or k < 0 else "YES")