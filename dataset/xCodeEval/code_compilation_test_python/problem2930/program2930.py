def program2930():
    OGticket = list(str(input()))
    n = map(int, OGticket)
    
    Sum1 = n[0] + n[1] + n[2]
    Sum2 = n[3] + n[4] + n[5]
    
    if Sum1>Sum2:
        LilNum = [n[3],n[4],n[5]]
        BigNum = [n[0],n[1],n[2]]
    elif Sum2>Sum1:
        LilNum = [n[0],n[1],n[2]]
        BigNum = [n[3],n[4],n[5]]
    else:
        LilNum = [0,0,0]
        BigNum = [0,0,0]
    
    LilNum.sort()
    BigNum.sort()
    diff = abs(Sum1-Sum2)
    
    
    
    if diff == 0:
        print "0"
    elif diff <= 9-LilNum[0] or diff <= BigNum[2]:
        print "1"
    elif diff <= 9-LilNum[0] + 9-LilNum[1] or diff <= 9-LilNum[0] + BigNum[3] or diff <= BigNum[2] + BigNum[1] 
        print "2"
    else:
        print "3"