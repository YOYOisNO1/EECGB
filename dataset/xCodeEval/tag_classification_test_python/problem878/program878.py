def program878():
    a,b,c = map(int , input().split())
    print(2*min(a,b)+2*c+(max(a,b)-min(a,b)>0))