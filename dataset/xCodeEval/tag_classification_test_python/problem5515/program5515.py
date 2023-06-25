def program5515():
    s1,v1,v2,t1,t2 = map(int,input().split())
    a=s1*v1+t1*2
    b=s1*v2+t2*2
    if a==b:print("Friendship")
    if a<b:print("First")
    if a>b:print("Second")