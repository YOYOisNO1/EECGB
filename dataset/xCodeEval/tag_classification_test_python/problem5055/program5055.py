def program5055():
    i=lambda:map(int,input().split());n,d=i();d-=sum(i());print([d//5,-1][d<10*(n-1)])