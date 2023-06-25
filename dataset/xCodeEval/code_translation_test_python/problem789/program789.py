def program789():
    a = map(int, input().split())
    a = sorted(a)
    lis = []
    lis.append(sum(a))
    if a[-1] == a[-2] and a[-2] == a[-3]:
    	lis.append(a[0]+a[1])
    if a[-1] == a[-2]:
    	lis.append(a[0]+a[1]+a[2])
    if a[-2] == a[-3] and a[-3] == a[-4]:
    	lis.append(a[0]+a[4])
    if a[-2] == a[-3]:
    	lis.append(a[0]+a[1]+a[4])
    if a[-3] == a[-4] and a[-4] == a[-5]:
    	lis.append(a[3]+a[4])
    if a[-3] == a[-4]:
    	lis.append(a[0]+a[3]+a[4])
    if a[-4] == a[-5]:
    	lis.append(a[2]+a[3]+a[4])
    print(min(lis))