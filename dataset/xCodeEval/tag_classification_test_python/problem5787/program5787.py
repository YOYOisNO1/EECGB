def program5787():
    n = int(input())
    ar = list(map(int, input().split()))
    min_val = min(ar)
    min_count = len([x for x in ar if x == min_val])
    
    if min_count > n//2:
        print("Bob")
    else:
        print("Alice")
    
    