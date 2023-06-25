def program1456():
    
    n=int(input() )
    l=set()
    
    
    t1=list (map(int,input ().split ()))
    t2=list (map(int,input ().split ()))
    l=set(t1+t2)
    
    nb=0
    for i in range (n) :
        for j in range (n) :
                   if (t1[i]^t2[j]) in l :
                       nb+=1
    
    if (nb%2==0):
                  print('Karen')
    else:
                  print('Koyomi')
                  
        
                   