def program901():
    a=int(input());i=0
    while(a>=0):i+=1;a-=i*(i+1)/2
    print(i-1)