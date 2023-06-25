def program361():
    from collections import Counter
    
    n = int(input())
    a = [int(s) for s in input().split()]
    
    print(Counter(a).most_common(1)[0][1])