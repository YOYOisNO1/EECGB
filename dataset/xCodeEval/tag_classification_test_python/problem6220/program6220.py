    '''input
    5 5 5 6
    ''' 
    from math import ceil, sqrt 
def main(): 
         r1, c1, r2, c2 = map(int, input().split())
         #rook 
         if r1 == r2 and c1 != c2: 
            rook = 1 
         elif r1 != r2 and c1 == c2:
            rook = 1 
         elif r1 != r2 and c1 != c2: 
            rook = 2 
         else: 
            rook = 0 
            
         #bishop 
         if(r1 + c1)%2 == 0 and (r2 + c2)%2 != 0: 
            bishop = 0 
         elif (r1 + c1)%2 != 0 and (r2 + c2)%2 == 0: 
            bishop = 0 
         else: 
            try: 
                if (c2 - c1)/(r2 - r1) == 1 or (c2 - c1)/(r2 - r1) == -1: 
                    bishop = 1 
                else: 
                    bishop = 2 
            except: 
                bishop = 2 
                
                
         #king 
         d1, d2 = 0,0
         if r1 > r2:
            d1 = r1-r2
            
         if c1 > c2:
            d2 = c1- c2
            
         if d1 > 0:
            r2 = r1 + d1
    
         if d2 > 0:
            c2 = c1 + d2
         
         king = 0
    
         # print(d1, d2)
         # print(r1, r2, c1, c2)
         while True:
            if r1 == r2 and c1 != c2:
                flag = 1
                break
                
            if c1 == c2 and r1 != r2:
                flag = 2
                break
                
            if abs(r1 - r2) == abs(c1 - c2):
                flag = 3
                break
                
            r1 += 1
            c1 += 1
            king += 1
         
         
         # print(flag, king)
    
         if flag == 1:
            king += abs(c1-c2)  
         elif flag == 2:
            king += abs(r1 - r2)
         elif flag == 3:
            king += ceil(sqrt((r1-r2)**2 + (c1-c2)**2)/sqrt(2))
         
            
            
         print(rook, bishop, king) 
         
         
    if __name__ == "__main__": 
        main()