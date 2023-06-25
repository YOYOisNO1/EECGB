def program689():
    ak=list(map(int,input().split()))
    ak.sort()
    ds=ak[1]
    ds=abs(ak[0]-ds)+abs(ak[2]-ds)
    print(ds)