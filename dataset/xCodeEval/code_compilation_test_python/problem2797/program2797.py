def program2797():
    td,pd,sp,g,r = map(int,input().split())
    it = pd/sp
    if(it<g):
        ntt = td/sp
        print("%.8f" %ntt )
    else:
        nt = r+g+((td-pd)/sp)
        print("%.8f" % nt)