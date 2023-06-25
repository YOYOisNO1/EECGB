def program4522():
    import math
    
    while 1:
        try: n=int(input())
        except: break
        ds=[]
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                ds.append(i)
                if i!=n//i:
                    ds.append(n//i)
        for d in sorted(ds,reverse=True):
            for x in range(2,int(math.sqrt(d))+1):
                if d%(x*x)==0:
                    break
            else:
                print(d)
                break