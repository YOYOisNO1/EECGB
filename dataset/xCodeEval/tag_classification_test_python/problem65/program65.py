def program65():
    n, p, left, right = map(int, input().split())
    summ = 0
    if p < left:
        summ = (left - p) + 1 + ((right - left) + 1) * (right < n)
    elif p > right:
        summ = (p - right) + 1 + ((right - left) + 1) * (left > 1)
    else:
        if p - left < right - p:
            summ = ((p - left) + 1 + (p - left) * (right < n)) * (left > 1)
            summ += ((right - p) + 1) * (right < n)
        else:
            summ = ((right - p) + 1 + (right - p) * (left > 1)) * (right < n)
            summ += ((p - left) + 1) * (left > 1)
    
    print(summ)