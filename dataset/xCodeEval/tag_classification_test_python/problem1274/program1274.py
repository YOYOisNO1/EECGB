    str=input()
    a=str.split()
    
def len(x1,y1,x2,y2):
        return (y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1)
    
    for x in xrange(0,6):
        a[x]=int(a[x])
    if(len(a[0],a[1],a[2],a[3])==len(a[2],a[3],a[4],a[5]) and ((a[5]-a[3])*(a[2]-a[0])!=(a[4]-a[2])*(a[3]-a[1]))):
        print('Yes')
    else:
        print('No')