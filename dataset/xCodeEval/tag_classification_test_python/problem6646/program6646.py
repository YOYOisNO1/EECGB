def program6646():
    n,m = map(int,input().split());
    mod = 10**9 + 7;
    ans = 0;
    if m != 1:
    	ans = pow(2*m - 1,n,mod)
    	ans -= pow(m,n,mod);
    	ans *= m; ans %= mod;
    	ans *= pow(m-1,mod - 2,mod); ans %= mod;
    	ans += pow(m,n,mod);
    	ans = (ans%mod + mod)%mod;
    else:
    	ans = n + 1;
    print(ans;)