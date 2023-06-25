    import sys
    
    
    array = input().split(" ")
    a,b,x,y = int(array[0]) , int(array[1]), int(array[2]), int(array[3])
        
    
def pgcd(a,b):
        """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
        while b != 0:
            r=a%b
            a,b=b,r
        return a
        
    # p = PGCD_x_y(x,y)
    p = pgcd(x,y)
    # print(a,b,x,y)
    # print(p)
    k1 = a//(x/p)
    k2 = b//(y/p)
        
    if k1 < k2 : 
        print(int(k1))
    else : 
        print(int(k2))