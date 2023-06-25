def program1889():
    N, A = map(int, input().split())
    problems = []
    for i in range(N):
        a, b = map(int, input().split())
        problems.append((a, b))
    problems.sort()
    ans = 0
    while ans < N and A >= problems[ans][0]:
        A += problems[ans][1]
        ans += 1
    print(ans)