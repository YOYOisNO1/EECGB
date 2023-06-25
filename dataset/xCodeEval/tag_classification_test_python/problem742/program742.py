def program742():
    n , m = map (int , input().split ())
    ans = [0] * n
    l , r = 0 , n - 1
    j = n - 2 
    for i in range (n - 1) :
    	if m > (1 << j) :
    		m = m - (1 << j)
    		ans[r] = i + 1
    		r -= 1
    	else :
    		ans[l] = i + 1
    		l += 1
    	j -= 1
    ans[l] = n
    print(' ').join ([str (v) for v in ans])