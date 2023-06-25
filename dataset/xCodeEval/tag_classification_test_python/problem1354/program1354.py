def program1354():
    n, m, k = map(int, input().split())
    m -= 1
    prices = list(map(int, input().split()))
    left = m - 1
    right = m + 1
    
    leftbest = 101
    rightbest = 101
    
    while left >= 0:
        if prices[left] < leftbest and prices[left] <= k and prices[left] != 0:
            leftbest = prices[left]
            break
        else:
            left -= 1
            
    while right < n:
        if prices[right] < rightbest and prices[right] <= k and prices[right] != 0:
            rightbest = prices[right]
            break
        else:
            right += 1
    
    if leftbest == 101:
        meters = (right - m) * 10
    elif rightbest == 101:
        meters = (m - left) * 10
    else:
        meters = (min(m - left, right - m)) * 10
    
    print(meters)