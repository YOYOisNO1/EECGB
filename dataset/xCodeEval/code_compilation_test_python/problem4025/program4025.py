    # To change this template, choose Tools | Templates
    # and open the template in the editor.
    
    __author__="yaroslav"
    __date__ ="$02.08.2011 18:00:13$"
def f(x,p1,p2,p3,p4):
        return (((x % p1) % p2) % p3) % p4
    
    if __name__ == "__main__":
        inp = input()
        input = inp.rsplit(' ')
        p1 = int(input[0])
        p2 = int(input[1])
        p3 = int(input[2])
        p4 = int(input[3])
        a = int(input[4])
        b = int(input[5])
        allkol=0
        list1 = range(a+1,b)
        list1.append(a)
        for x in list1:
            kol = 0
            for i in [p1,p2,p3,p4]:
                for j in [p1,p2,p3,p4]:
                    if j!=i:
                        for k in [p1,p2,p3,p4]:
                            if k not in(j,i):
                                for m in [p1,p2,p3,p4]:
                                    if m not in (j,i,k):
                                        if x==f(x,i,j,k,m):
                                            kol+=1
            if kol>7:
                allkol+=1
        print allkol