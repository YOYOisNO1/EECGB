def HasDistinctDigits(nstr):
        digs=[]
        for i in nstr:
            digs.append(int(i))
        distinct_digs=[]
        #print(digs)
        for i in nstr:
            if int(i) not in distinct_digs:
                distinct_digs.append(int(i))
        for i in distinct_digs:
            if int(i) in digs:
                digs.remove(int(i))
        #print(digs)
        if len(digs)==0:
            return True
        else:
            return False
    
    n=int(input())
    
    for i in range(n+1,10000):
        if HasDistinctDigits(str(i)):
            print(i)
            break