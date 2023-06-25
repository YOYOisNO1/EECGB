def program428():
    n, d = map(int, input().split(" "))
    s = list(map(int, input().split(" ")))
    l = [list(i for i in s if s[i] = 1)]
    diff = [list(l[i+1] - l[i] if  (l[i+1] - l[i]) <= d) else -1 if (l[i+1] - l[i]) > d) for i in range(0, len(l) - 1))]
    print(min(diff))