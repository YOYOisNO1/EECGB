def program4038():
    *a,d=map(int,input().split())
    a,b,c=sorted(a)
    
    print(max(0,(d-(b-a))+ max(0,d-(c-b))))