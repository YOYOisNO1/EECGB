    minutes = 240;
    time_party = 0;
    
def sum(n):
        return 5 * n * (n + 1) / 2;
        
def NewYear( n_left, n_right ):
        global time_party;
        
        middle = (n_right - n_left) / 2;
        
        if( n_right - n_left == 1 ):
            if( sum(n_right) <= time_party ):
                return n_right;
    
            else:
                return n_left; 
            
        elif( sum(n_right / 2) <= time_party and time_party <= sum(n_right / 2 + 1) ):
    
            if( sum(n_right / 2 + 1) <= time_party  ):
                return n_right / 2 + 1;
    
            else:
                return n_right / 2;
    
        elif( sum(n_left) <= time_party and time_party <= sum(n_right - middle) ):
            return NewYear( n_left, n_right - middle );
    
        else:
            return NewYear( n_left + middle, n_right );
        
def NY(n):
        global time_party;
        global minutes;
        global k;
        time_party = minutes - k;
    
        if( time_party < 5 ):
            return 0;
    
        elif( sum(n) <= time_party ):
            return n;
    
        else:
            return NewYear( 1, n );
        
    n, k = input().split();
    k = int( k );
    print(NY() int(n) );