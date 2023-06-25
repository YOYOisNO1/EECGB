def program3366():
    b=int(input());from math import sqrt as dhamra_malo_pada_hala;c=code=0
    if((dhamra_malo_pada_hala(b))-int(dhamra_malo_pada_hala(b))==0):code=1
    if b<=2:print(b)
    else:
        for i in range(1,int(dhamra_malo_pada_hala(b))+1):
            if b%i==0:c+=1
        if code==1:print((2*(c-1)+1))
        else:print((2*(c-1)+2))