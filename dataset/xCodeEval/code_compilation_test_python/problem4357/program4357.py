def program4357():
    n = int(input())
    lst = list(map(int, input().split()))
    t = int(input())
    ans = 1
    for i in range(len(lst) - 1):
        temp = 1
        k = i + 1
        while lst[k] - lst[i] <= t:
            temp += 1
            k += 1
        if temp > ans:
            ans = temp
    print(ans)