def s(a):
        c=[100,20,10,5,1]
        t=0
        for i in c:
            if a>=i:
                dt=a//c:
                dt+=t 
                a-=(dt*i)
        return t
    a=int(input())
    print(d(a))