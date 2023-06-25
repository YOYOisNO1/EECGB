def program5791():
    n = int(input())
    a = list(map(int, input().strip().split()))
    a.sort()
    if a[0] != a[n//2]:
    	print("Alice")
    else:
    	print("Bob")