def program1284():
    #http://codeforces.com/contest/994/problem/0
    n,m = map(int,input().split())
    s=input().split()#[3,4,1,0] #
    f=input().split()##
    g=set(s)
    f=set(f)
    b=list(g&f)
    if len(b)>0:
        for i in b:
            print (i,end=" ")
    else
        print ("")