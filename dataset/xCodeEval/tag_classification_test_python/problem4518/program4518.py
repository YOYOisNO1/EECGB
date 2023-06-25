def program4518():
    N = int(input())
    S = list(map(int, input().split()))
    colors = [S[0]]
    for i in range(1, N):
        x = 2
        j = 0
        while j < len(colors):
            if S[i] % colors[j] == 0:
                x = 0
            elif x == 2 and colors[j] % S[i] == 0:
                colors = colors[:j] + [S[i]] + colors[j + 1:]
                x = 1
            elif x == 1 and colors[j] % S[i] == 0:
                colors.pop(j)
                j -= 1
            j += 1
        if x == 2:
            colors.append(S[i])
    print(len(colors))