def program3504():
    t1 = map(int, input().split(':'))
    t1 = t1[0]*60 + t1[1]
    t2 = map(int, input().split(':'))
    t2 = t2[0]*60 + t2[1]
    ans = (t2+t1)/2
    h = str(ans/60)
    if len(h) == 1:
    	h = '0' + h
    m = str(ans%60)
    if len(m) == 1:
    	m = '0' + m
    print(h+) ':' + m