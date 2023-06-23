def program160():
    for i in range(int(input())):
        n, k, d = map(int, input().split())
        s = list(map(int, input().split()))
        ch = set()
        for i in range(n - d):
            ch.add(len(set(s[i:i + d])))
        print(min(ch))