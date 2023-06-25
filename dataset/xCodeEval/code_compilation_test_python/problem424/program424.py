    #! /usr/bin/python
    
    __author__="Guillermo Candia Huerta"
    __date__ ="$10-06-2010 11:06:16 AM$"
    
def es_primo(n):
        if n == 2 or n == 3 or n == 5: return True
    
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    
def Noldbach(n):
        #print n
        for a in range(0, len(l)):
            #print 'a =' + str(a) + 'suma=' + str(1 + l[a] + l[a+1]) +'n='+ str(n)
            suma = 1 + l[a] + l[a+1]
            if suma == n:
                return True
            if suma >n:
                break
        return False
    
    
    
    
        
    
    if __name__ == "__main__":
        n, k = map(int, input().split())
    
        l = filter(es_primo, range(2,1000))
        ln = filter(Noldbach, l)
    
        print l
        print ln
        for a in range(n+1):
            if a in l:
                k = k - 1
                if k == 0:
                    salida = 'YES'
                    break
            salida = 'NO'
    
        print salida
    
        
    