def program3099():
    
     r=p=1
    for d in map(int,input()[::-1]):r=max(d*r,(d-1)*p);p*=9
    print(max(r,p//9))