def program6090():
    from math import log
    
    if __name__=='__main__':
        s = input()
        x = int(s[:-1])
        seat = 'fedabc'.index(s[-1])+1
        
        phase = (x-1)/4
        serve = phase*12
        
        move = phase*4
        if (x-phase*4)<=2: 
            dmove = x-phase*4-1
            serve += dmove*6
        else: 
            dmove = x-phase*4-3
            serve += dmove*6
        move += dmove
        #~ print(serve,) move, seat
        print(serve+move+seat) 