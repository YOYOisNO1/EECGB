def program6419():
    # maa chudaaye duniya
    fib = [0, 1]
    for i in range(2, 100002):
        fib.append(fib[i-1]+fib[i-2])
    # print(fib[:10])
    n, m = map(int, input().split())
    ans = 2*(fib[n+1] + fib[m+1] - 1)
    print(ans%(10**9 + 7))