def program4753():
    I=lambda:map(int,input().split())
    a,b,c=I()
    x,y,z=I()
    a=x-a,y-b,z-c
    print(["No","Yes"][sum(map(lambda x:(-x)//2,filter(lambda x:x<0,a)))>=sum(filter(lambda x:x>0,a))])