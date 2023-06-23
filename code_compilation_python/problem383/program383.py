def program383():
    n = int(input())
    dip = []
    rewarded = [0]*3
    for _ in range(3):
        a = list(map(int, input().split()))
        a[1] = a[1] - a[0]
        dip.append(a)
    for i in range(3):
        n -= dip[i][0]
        rewarded[i] += dip[i][0]
    while n>0:
        if dip[0][1] > 0:
            if n >= dip[0][1]:
                rewarded[0]+=dip[0][1]
                n-=dip[0][1]
                dip[0][1] = 0
            else:
            	rewarded[0] += n
                n = 0
                dip[0][1] = 0
        elif dip[1][1] > 0:
            if n>=dip[1][1]:
                rewarded[1]+=dip[1][1]
                n-=dip[1][1]
                dip[1][1]=0
            else:
                rewarded[1] += n
                n = 0
                dip[1][1] = 0
        else:
            rewarded[2] += n
            n = 0
    
    for i in rewarded:
    	print(str(i), end=" ")