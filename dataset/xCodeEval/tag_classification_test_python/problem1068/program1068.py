def program1068():
    max=(int(input()))
    max=0
    min=0
    a=[ int(j) for j in input().split()]
    a.append(a[0])
    b=[ int(j) for j in input().split()]
    b.append(b[0])
    for i in range(3):
    	if a[i]<=b[i+1]:
    		max+=a[i]
    	else:
    		max+=b[i+1]
    	if a[i+1]-b[i]-b[i+1]>0:
    		min+=a[i+1]-b[i]-b[i+1]
    print(min, max)