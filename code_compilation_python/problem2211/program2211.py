    # -*- coding: utf-8 -*-
    """
    Created on Fri Jun 26 19:19:34 2020
    
    @author: UV
    """
def main():
        tamaño_del_ciclo = int(input())
        k=0
        for a in range(2, tamaño_del_ciclo+1):
            if a%2 ==0:
                k=3*(k+1)
               
            else:
                k = 3*(k-1)
        print(k)
            
        
    if __name__=="__main__":
        main()