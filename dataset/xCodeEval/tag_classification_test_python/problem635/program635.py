def program635():
    n = int(input())
    a = map(int, input().split(' '))
    a = sorted(a)
    for i in range(n-2):
    	if a[i] + a[i+1] > a[i+2]:
    		print("YES")
    		exit()
    print("NO")