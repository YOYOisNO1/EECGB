def program241():
    n, k, x = map(int, input().split())
    balls = list(map(int, input().split()))
    
    
    ans = 0
    for i in range(n - 1):
        if balls[i] == x and balls[i + 1] == x:
            curr = 2
            temp = balls[:i] + balls[i + 2:]
            while True:
                j = 0
                found = False
                while j < len(temp) - 1:
                    k = j + 1
                    while k < len(temp) and temp[k] == temp[j]:
                        k += 1
                    if k - j >= 3:
                        curr += k - j
                        temp = temp[:j] + temp[k:]
                        found = True
                        break
                    j += 1
                if not found:
                    break
            ans = max(ans, curr)
    print(ans)