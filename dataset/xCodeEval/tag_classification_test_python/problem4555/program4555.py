def diploma():
        IPT = []
        ipt = input()
        Ipt = ipt.split()
        for x in Ipt:
            IPT.append(int(x))
        n = IPT[0]
        k = IPT[1]
        C = 0
        D = 0
        R = int(n/2)
        C = (int(R/(k+1)))
        D = (C*k)
        print(str(int(C))+' '+str(int(D))+' '+str(int(n-C-D)))
    
    diploma()