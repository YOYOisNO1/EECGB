def program1377():
    read=lambda:map(int,input().split())
    n=input()
    mi1,mx1=read()
    mi2,mx2=read()
    mi3,mx3=read()
    
    d1=mi1
    d2=mi2
    d3=mi3
    n-=(mi1+mi2+mi3)
    if(n>0):
        if(n>(mx1-mi1)):
            d1=mx1
            n-=(mx1-mi1)
        else:
            d1+=n
            n=0
    if(n>0):
        if(n>(mx2-mi2)):
            d2=mx2
            n-=(mx2-mi2)
        else:
            d2+=n
            n=0
    d3+=n
    print(d1,d2,d3)
    
    
        
    
    