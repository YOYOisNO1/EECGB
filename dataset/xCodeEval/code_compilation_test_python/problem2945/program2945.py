def program2945():
    l = [int(i) for i in input().split(' ')]
    ans = 0
    curf = l[1]-l[2]
    for i in range(l[3]-1):
        if curf<0:
            ans = -1
                break
    	req = (l[0]-l[2])*2*((i+1)%2)+l[2]*2*(i%2)
    	if curf<req:
    		curf=l[1]
    		ans+=1
    	curf-=req
    if (l[3]%2 == 0 and curf<l[2]) or (l[3]%2 == 1 and curf<l[0]-l[2]) and ans!=-1:
    	ans+=1
    print ans