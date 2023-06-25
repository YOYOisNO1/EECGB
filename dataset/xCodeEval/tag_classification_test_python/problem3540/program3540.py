def program3540():
    n,t=map(int,input().split(' '))
    s=input()
    l=[]
    for i in xrange(t):
        s=s.replace("BG","GB",s.count("BG"))
        l.append(s)
    print(l[-1])