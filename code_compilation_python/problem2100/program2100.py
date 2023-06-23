    a=[]
    b=[]
def ok(a):
        a.sort()
        if a[0][0]!=a[1][0] or a[0][0]!=a[2][0]: return False;
        if a[0][0]==a[3][0] or a[3][0]!=a[4][0] or a[3][0]==a[5][0]: return False;
        if a[5][0]!=a[6][0] or a[5][0]!=a[7][0]: return False;
        return True
        
    for i in xrange(8):
        c=map(int,input())
        a.append( c )
        b.append( [c[1],c[0]])
    
    if ok(a) and ok(b):
        print "respectable"
    else:
        print "ugly"
    