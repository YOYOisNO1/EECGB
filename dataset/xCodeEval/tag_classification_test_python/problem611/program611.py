def program611():
    n,k=map(int,input().split())
    time=240-k
    i=1
    while time>=0:
       time-=5*i
       i+=1
    if n>(i-2):
        print(i-2)
    else:
        print(n)