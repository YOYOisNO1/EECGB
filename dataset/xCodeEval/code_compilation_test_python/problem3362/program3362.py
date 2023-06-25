    is_valid=1
    is_error=0
    mp=[-1,31,28,31,30,31,30,31,31,30,31,30,31]
    dbm=[-1]
    db=0
    for dim in mp:
    	dbm.append(db)
    	db+=dim
    
def is_leap_year(year):
    	if year%4==0 and year%100==0:
    		return 1
    	elif year%4==0:
    		return 1
    
def dby(year):
    	nyear=year-1
    	return nyear*365+nyear//4-nyear//100+nyear//400
    
def calc_days_in_month(month,year):
    	if month==2:
    		if is_leap_year(year)==1:
    			return 29
    		else:
    			return 28
    	return mp[month]
    
def days_previous_month(month,year):
    	return dbm[month]+(month>2 and is_leap_year(year))
    
def no_of_days_from_start(year,month,day):
    	return dby(year)+days_previous_month(month,year)+day
    
    
    f=open("input.txt","r")
    T=f.readline()
    D=T.split()
    f.close()
    
    D1=D[0].split("/")
    D2=D[1].split("/")
    
    
    d1=int(D1[0])
    m1=int(D1[1])
    y1=int(D1[2])
    
    
    
    d2=int(D2[0])
    m2=int(D2[1])
    y2=int(D2[2])
    
    if d1<1 or d1>calc_days_in_month(m1,y1) or m1<1 or m1>12:
    	is_error=1
    
    if d2<1 or d2>calc_days_in_month(m2,y2) or m2<1 or m2>12:
    	is_error=1
    
    if y1<2019: 
    	is_valid=0
    if y2<2019:
    	is_valid=0
    
    if y1==2019 :
    	if m1==12:
    		if d1<30:
    			is_valid=0
    	else:
    		is_valid=0
    
    if y2==2019:
    	if m2==12:
    		if d2<30:
    			is_valid=0
    	else:
    		is_valid=0
    
    tot_no_of_days1=no_of_days_from_start(y1,m1,d1)
    tot_no_of_days2=no_of_days_from_start(y2,m2,d2)
    
    w1=tot_no_of_days1
    w2=tot_no_of_days2
    
    if w1>w2:
    	is_valid=0
    
    
    temp=tot_no_of_days1//7
    w1-=2*temp
    temp=tot_no_of_days1%7
    if temp==0:
    	w1-=1
    elif temp>=1:
    	w1-=2
    
    
    temp=tot_no_of_days2//7
    w2-=2*temp
    temp=tot_no_of_days2%7
    if temp==0:
    	w2-=1
    elif temp>=1:
    	w2-=2
    
    
    f=open("output.txt","w")
    if is_error==1:
    	f.write("error")
    elif not is_valid ==1:
    	f.write("invalid")
    else:
    	ans=w2-w1
    	if tot_no_of_days1%7!=0 and tot_no_of_days1%7!=1:
    		ans+=1
    	f.write(str(ans))
    f.close()