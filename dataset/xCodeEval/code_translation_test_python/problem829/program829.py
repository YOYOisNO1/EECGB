def program829():
    from datetime import date
    a,b=input(),input()
    d={'monday': 0, 'tuesday': 1,'wednesday': 2, 'thursday': 3,'friday':4, 'saturday':5, 'sunday':6}
    ans=0
    for i in range(2000,2029):
     if i%4!=0:
      for j in range(1,12):
       if date(i,j,1).weekday()==d[a] and  date(i,j+1,1).weekday()==d[b]:
        ans=1
        break
    print('YES') if ans==1 else 'NO'   
       