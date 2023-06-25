def program795():
    l=['January','February','March','April','May','June','July','August','September','October','November','December']
    s=input()
    n=int(input())
    x=0
    for i in range(12):
        if(s==l[i]):
            x=i
    print(l[(x+n)%12])