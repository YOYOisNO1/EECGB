def program2494():
    h=(input())
    v=(input())
    hv=(int(h,2)^int(v,2))
    print('{0:>0{w}b}'.format(hv,w=len(h)))