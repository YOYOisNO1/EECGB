def program1532():
    a,b,c,d = [int(x) for x in input().split(" ")]
    if((a/b)<(c/d)): 
        x=(b*c-a*d)
        y=b*c
        for i in range(2,min(x,y)+1):
            while(x%i==0 and y%i==0):
                x//=i
                y//=i
        print(x,'/',y,sep="")
    elif((a/b)>(c/d)):
        x=(a*d-b*c)
        y=a*d
        for i in range(2,min(x,y)+1):
            while(x%i==0 and y%i==0):
                x//=i
                y//=i
        print(x,'/',y,sep="")
    else: print("0/1")