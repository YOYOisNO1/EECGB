def program4862():
    first=list(map(int, input().split()))
    second=list(map(int, input().split()))
    
    xmax=max(first[::2])
    xmin=min(first[::2])
    ymax=max(first[1::2])
    ymin=min(first[1::2])
    fircenx=sum(first[::2])
    firceny=sum(first[1::2])
    seccenx=sum(second[::2])
    secceny=sum(second[::2])
    
    first.extend((fircenx, firceny))
    second.extend((seccenx, secceny))
    mysum=[ second[2*i]+second[2*i+1] for i in range(4)]
    mydif=[ second[2*i+1]-second[2*i] for i in range(4)]
    
    summax=max(mysum)
    summin=min(mysum)
    difmax=max(mydif)
    difmin=min(mydif)
    
    for i in range(5):
        a= first[2*i]+first[2*i+1]
        b=first[2*i+1]-first[2*i]
        if i==4:
            summin*=4; summax*=4; difmin*=4; difmax*=4;
            
        if summin <= a <= summax and difmin <= b <= difmax:
            print("YES")
            exit()
    
    
    for i in range(4):
        if i==4:
            xmin*=4; xmax*=4; ymin*=4; ymax*=4;
        if xmin <= second[2*i] <= xmax and ymin<=second[2*i+1]<=ymax:
            print("YES")
            exit()
    
    
    
    print("NO")