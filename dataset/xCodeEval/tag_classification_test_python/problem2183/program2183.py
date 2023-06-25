def program2183():
    n, c = list(map(int, input().split()))
    p = list(map(int, input().split()))
    t = list(map(int, input().split()))
    fi = 0
    se = 0
    ti = 0
    for i in range(n):
        ti += t[i]
        fi += max(0, p[i] - c * ti)
    ti = 0
    for i in range(n - 1, -1, -1):
        ti += t[i]
        se += max(0, p[i] - c * ti)
    ret = ["Limak", "Radewoosh", "Tie"]
    pos = 2
    if fi > se:
        pos = 0
    elif fi < se:
        pos = 1
    print(ret[pos])