def program4371():
    import sys
    from collections import Counter
    
    #sys.stdin = open("input.txt")
    #sys.stdout = open("output.txt", "w")
    
    n, t = [int(i) for i in input().split()]
    lst = [int(i) for i in input().split()]
    cnt = Counter(lst)
    mostlst = cnt.most_common()
    freq = mostlst[0][1]
    
    lst = lst * 2
    
    n, m = len(lst), n
    d = [1 for i in range(n)]
    #print(lst)
    for i in range(n):
    	for j in range(0, i):
    		if lst[j] <= lst[i]:
    			d[i] = max(d[i], d[j] + 1)
    
    most_in_one = max(d[:n//2])
    most_in_two = max(d)
    #print(freq)
    #print(most_in_one)
    #print(most_in_two)
    ans = most_in_one + freq * (t - 1)
    if t > 1:
    	ans = max(ans, most_in_two + freq * (t - 2))
    print(ans)