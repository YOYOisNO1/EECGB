def day_number(d,m,y):
        
        res = d
        #defino los meses
        meses = [31,28,31,30,31,30,31,31,30,31,30,31] 
        
        if (m!=1): #dias del año corriendo
            for i in range (m-1):
                res = res + meses[i]
            if ( año_bisiesto(y) == True and m > 2):
                res = res + 1
    
        i = 1
        while (i < y):
            if ( año_bisiesto(i) == False ):
                res = res + 365
            else:
                res = res + 366
            i = i + 1
    
        return res
    
def año_bisiesto(año):
        if(año%4 ==0 ):
            if(año%100 ==0):
                if(año%400 ==0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    
    a = list(map(int,input().split(':')))
    b = list(map(int,input().split(':')))
    print(abs(day_number(a[2],a[1],a[0])-day_number(b[2],b[1],b[0])))