def program2827():
    a1, b1 = [int(d) for d in input().split()]
    a2, b2 = [int(d) for d in input().split()]
    a3, b3 = [int(d) for d in input().split()]
    ans = ""
    if a2 + a3 <= a1 and b2 <= b1 and b3 <= b1:
    	ans = "YES"
    elif a2 + b3 <= a1 and b2 <= b1 and a3 <= b1:
    	ans = "YES"
    elif b2 + b3 <= a1 and a2 <= b1 and a3 <= b1:
    	ans = "YES"
    elif b2 + a3 <= a1 and a2 <= b1 and b3 <= b1:
    	ans = "YES"
    elif a2 + a3 <= b1 and b2 <= a1 and b3 <= a1:
    	ans = "YES"
    elif a2 + b3 <= b1 and b2 <= a1 and a3 <= a1:
    	ans = "YES"
    elif b2 + b3 <= b1 and a2 <= a1 and a3 <= a1:
    	ans = "YES"
    elif b2 + a3 <= b1 and a2 <= a1 and b3 <= a1:
    	ans = "YES"
    else: ans = "NO"
    print(ans)