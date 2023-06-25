# def fun( num ) :
    #     prob = 1
    #     if(num>0):
    #         # print( "prob" , prob )
    #         print( "num" , num )
    #         prob *= num
    #         prob *= fun( num-1 )
    #     return prob
    
    # print( fun( 8 ) )
    
    save={}
    
def fun( w , b ) :
        global save
        key=str(w)+' '+str(b)
        if(save.get(key)!=None):
            return save[ key ]
    
        prob=0
        if (( w>= 0 ) and ( b>=0 ) and ( (w+b)!= 0 ) ) :
            prob = w / ( w + b  )
            if( (w+b)>2 ):
                prob += fun( w-1 , b-2 ) * ( b / ( w+b ) ) * ((b-1) / ( w+b-1 ) ) * ( w / ( w+b-2 ))
                prob += fun( w , b-3 ) * ( b / ( w+b  ) ) * ( (b-1) / ( w+b-1 ) ) * ( (b-2) / ( w+b-2 ))
        save[ key ]=prob
        return prob
    
    scr = input()
    mice_w , mice_b =map(int , scr.split())
    
    prob = fun( mice_w , mice_b )
    
    print( prob )