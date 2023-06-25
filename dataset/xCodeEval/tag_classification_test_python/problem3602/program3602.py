def program3602():
    length, times= map(int, input().split(" "))
    s=list(input())
    k=True
    if ("G" not in s or "B" not in s):
        k=False
    t=True
    if (k):
        for i in range(times):
            for i in range(len(s)-1, 0, -1):
                if (s[i]=="G" and s[i-1]=="B" and t):
                    del s[i]
                    s.insert(i-1, "G")
                    t=False
                else:
                    t=True
    print("".join(s))