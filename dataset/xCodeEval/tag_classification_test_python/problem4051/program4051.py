def judgeTwoPoints( pa , pb ):
        if pa[0] != pb[0] and pa[1] != pb[1]:
            #print( "ok!" , pa , pb , abs( pa[0] - pb[0] ) * abs( pa[1] - pb[1] ) )
            return abs( pa[0] - pb[0] ) * abs( pa[1] - pb[1] )
        else:
            return -1
    
def solve( pts , n ):
        if n == 1:
            return -1
    
        pts.sort()
        if n == 2:
            return judgeTwoPoints( pts[0] , pts[1] )
        if n == 3:
            resa = judgeTwoPoints( pts[0] , pts[1] )
            resb = judgeTwoPoints( pts[1] , pts[2] )
            resc = judgeTwoPoints( pts[0] , pts[2] )
            return max( resa , resb , resc )
    
        return judgeTwoPoints( pts[1] , pts[2] )
    
    if __name__ == "__main__":
        n = int( input() )
        pts = []
        for _ in range(n):
            pts.append( tuple([int(x) for x in input().split()]) )
    
        #print( pts )
        print( solve( pts , n ) )