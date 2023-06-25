    import sys
    
    
#def solve(a,b,c,d):
def solve(x):
        print(x)
        return x
    
    
    if __name__ == '__main__':
        IN = [x.strip() for x in sys.stdin.readlines()]
    
        n = int(IN[0])
        #a = [int(x) for x in IN[cur].split(' ')]
        ar,a_s,ap = [int(x) for x in IN[1].split(' ')]
        br,bs,bp = [int(x) for x in IN[2].split(' ')]
        #print(ar,a_s,ap)
        #print(br,bs,bp)
    
        # find min wins
        
        # how many can bob win?
        '''
        bob_wins = min(bp,ar) + min(br,a_s) + min(bs,ap)
        bp2 = bp-min(bp,ar)
        br2 = br-min(br,a_s)
        bs2 = bs-min(bs,ap)
        ar2 = ar-min(bp,ar)
        as2 = a_s-min(br,a_s)
        ap2 = ap-min(bs,ap)
        bob_ties = min(bp2,ap2) + min(br2,ar2) + min(bs2,as2)
        min_alice_wins = n-bob_wins-bob_ties
        '''
        min_alice_wins = max( ar-(br+bp), a_s-(br+bs), ap-(bs+bp), 0 )
        #print('bob_wins:',bob_wins)
        max_alice_wins = min(ap,br) + min(ar,bs) + min(a_s,bp)
        #print('alice_wins:',alice_wins)
        #print('{} {}'.format(n-bob_wins,alice_wins))
        print('{} {}'.format(min_alice_wins,max_alice_wins))
    