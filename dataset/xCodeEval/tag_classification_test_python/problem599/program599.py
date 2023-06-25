def program599():
    a=[int(x) for x in input().split()]
    a.sort()
    if a[2]>=a[0]+a[0]+a[1]+a[1]:
    	print(a[0]+a[1])
    else:
    	print(sum(a)//3)