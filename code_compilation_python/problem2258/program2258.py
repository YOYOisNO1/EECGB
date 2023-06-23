def program2258():
    
     y,b=list(map(int,input().split()))
    ny,ng,nb=list(map(int,input().split()))
    print(max(ng+ny*2-y,0)+max(ng+3*nb-b,0))