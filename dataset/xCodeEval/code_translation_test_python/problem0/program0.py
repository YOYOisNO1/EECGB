    inputc = input()
    sum1 = 0
    for c in inputc[0:3]:
    	sum1 += int(c)
    
    sum2 = 0
    for c in inputc[3:6]:
    	sum2 += int(c)
    
    # print(sum1,sum2)
    if sum1 == sum2 : 
    	print(0)
    	exit()
    
    cha =sum1-sum2 
    # print(cha)
    nums= map(int,inputc)
    avs1 = []
    for num in nums[0:3]:
    	avs1.append( 9-num )
    for num in nums[3:6]:
    	avs1.append(0-num)
    
    
    avs2 = []
    for num in nums[0:3]:
    	avs2.append( 0-num )
    for num in nums[3:6]:
    	avs2.append(9-num)
    
def cmpp(a,b):
    	if a<0:a=0-a
    	if b<0:b=0-b
    	return b-a
       
    avs1.sort(cmp=cmpp )
    avs2.sort(cmp=cmpp )
    
    avs=avs1
    if cha>0:
    	avs=avs2 
    count=1
    for av in avs:
    	if (av>0 and cha>0) or (av<=0 and cha <=0):
    		result=cha-av
    	if (av<= 0 and cha>0) or (cha<=0 and av>0):
    		result=cha +av
    
    	if cha>0:
    
    		if result>0:
    			cha=result
    			count+=1
    		else:
    			print(count)
    			break
    	else:
    		if result<0:
    			cha=result
    			count+=1
    		else:
    			print(count)
    			break