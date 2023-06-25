def program170():
    n, m, z = map(int, input().split());
    ans = 0;
    for i in range(z):
    	if (i+1)%n==0 and (i+1)%m==0:
    		ans = ans + 1;
    print(ans;)