def program2840():
       
        nbr = int(input()) ;
        s = input() ;
          res="" 
          res =res+s[0];
          i=1 
          cpt =0 ;
          while(i<nbr):
        
                if cpt == 0 :
                    d=s[i]
                    res +=s[i]
                    cpt +=1 
                    i +=1 
                else :
                    if s[i] == d :
                            i +=1 
                            cpt +=1
                    else :
                        cpt =0 ;
          return res