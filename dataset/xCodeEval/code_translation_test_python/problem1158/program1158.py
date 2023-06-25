def program1158():
    import sys; input = sys.stdin.readline
    s = input().strip()
    d = ("Danil", "Olya", "Slava", "Ann", "Nikita")
    g = 0
    for i in range(len(d)):
    	for j in range(len(s)-len(d[i])+1):
    		if s[j:j+len(d[i])] == d[i]: g += 1
    if g == 1: print("YES")
    else: print("NO")