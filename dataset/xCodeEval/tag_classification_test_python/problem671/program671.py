    '''
    Created on 2014/9/29
    
    @author: Yeu-Chern Harn
    '''
    import sys
def p471C( N ):
        diffH = 0
        Hlim = N
        for h in xrange(1, Hlim):
            rN = N - 2*h
            if rN % 3 == 0:
                rN = rN / 3
                if rN >= (h-1)*h/2:
                    diffH = diffH + 1
                else:
                    break
        return diffH
    
def p471C_2(N):
        diffH = 0
        sumVal = 0
        card = 2
        while sumVal + card <= N:
            sumVal = sumVal + card
            rN = N - sumVal
            if rN % 3 == 0:
                diffH = diffH + 1
            card = card + 3
        return diffH
    
    if __name__ == '__main__':
        iVal = long(input())
        diffH = p471C_2(  iVal )
        print(diffH)