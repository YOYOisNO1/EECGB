def the_Artful():
        n=int(input())
        x=list(map(int,input().split()));
        y=list(map(int,input().split()));
        cpt=0
        c1=set(x+y)
        for i in range(n):
            for j in range(n):
                h=x[i]^y[j]       
                if h in c1:
                    cpt+=1;
        if (cpt%2==0): 
            print('Karen')
        else:
            print('Kayomi')
       the_Artful ()
    
    