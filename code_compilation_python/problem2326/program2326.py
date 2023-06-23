def program2326():
    n=int(input())
    Lko=[]
    Lka=[]
    for i in range (n) :
        Lka.append(int(input()))
    for i in range (n):
        Lko.append (int(input()))
    
    E=set(Lko+Lka)
    
    c=0;
    for i in range(n) :
        for j in range(n) :
            c=c+(Lko[i]^Lka[j])in E) 
                
    
    if (c%2==0):
        print("Karen")
    else:
        print("Koyomi")