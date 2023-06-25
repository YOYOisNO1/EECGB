    pp = -1
def func(x) :
    	p = 6*N / (x + A);
    	p = max(p, B);
    	return p * (x + A);	
    read = lambda : map(int, input().split())
    N, A, B = read()
    l = 0; r = 10**9;
    for xx in range(100):
      m1 = l + (r - l) / 3;
      m2 = r - (r - l) / 3;
      if (func(m1) > func(m2)) : l = m1;
      else : r = m2;
    ans = 10**20;
    a = -1;
    b = -1
    for xx in range(l, r + 1):
    	res = func(xx);
    	if (res < ans) :
    		ans = res;
    		a = xx + A;
    		p = 6*N / (xx + A);
    		p = max(p, B);
    		b = p;
    print ans
    print a, b			
      		