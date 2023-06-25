def program2398():
    t= list(map(int,input().split(":")))
    x= t[0]*60+t[1]+int(input())
    a= int(x/60)
    b= x%60
    if a>=24:
        a= a%24
    if a<10:
        a= "0"+str(a)
    if b<10:
        b= "0"+str(b)
    s= a+":"+b
    print(s)