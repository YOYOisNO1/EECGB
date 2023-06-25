def program4716():
    n = int(input())
    min1, max1 = map(int, input().split())
    min2, max2 = map(int, input().split())
    min3, max3 = map(int, input().split())
    s = min1 + min2 + min3
    if s < n:
        min1 = min(max1, min1 + n - s)
    s = min1 + min2 + min3    
    if s < n:
        min2 = min(max2, min2 + n - s)
    s = min1 + min2 + min3
    if s < n:
        min3 = min(max3, min3 + n - s)
    print(min1, min2, min3)