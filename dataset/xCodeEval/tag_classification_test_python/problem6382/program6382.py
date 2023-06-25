def program6382():
    from collections import Counter
    
    counter = Counter(map(int, input().split()))
    
    if counter[1] >= 1 or counter[2] >= 2 or counter == Counter([2, 4, 4]) or counter == Counter([3, 3, 3]):
        print("YES")
    else:
        print("NO")