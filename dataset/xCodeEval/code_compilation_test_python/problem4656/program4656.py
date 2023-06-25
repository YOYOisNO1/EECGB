    import sys
    
def solve(a, b, c, d):
        #w=[a,b]
        #q=[c,d]
        #[q,p] in w
        #p?
        ind1 = 0
        ind2 = 0
        cnt1 = 0
        phases = []
        phases2 = []
        ahtung = False
        while True:
            if a[ind1] == c[ind2]:
                ind2 += 1
    
            if ind2 == len(c):
                ind2 = 0
                #contained. lets check syn
                if ind1 in phases:
                    #period!
                    #print "period!"
                    phases.append(ind1)
                    phases2.append(cnt1)
                    break
                phases.append(ind1)
                phases2.append(cnt1)
    
            ind1 += 1
            if ind1 == len(a):
                ahtung = (ind2!=0)
                ind1 = 0
                cnt1 += 1
    
            if cnt1 >= b:
                #all length of a reached
                return len(phases)/d
    
        #print phases
        #print phases2
        
        val = phases.pop(-1)
        cnt2 = len(phases)
        ind = len(phases) - phases[::-1].index(val) -1
        cnt2 -= ind
        #print "second in period = " + str(cnt2)
        per1 = phases2[-1] - phases2[ind]
        #print "first in period = " + str(per1)
    
        #print ahtung
        #if phases2[ind] == 0 or phases2[ind]==phases2[ind-1]:
        #    ahtung = False
        #else:
        #    ahtung = True
        #print ahtung
        res = cnt2 * b
    
        #if ahtung:
            res -= 1
        res /= (per1 * d)
        #print res
        if res<0:
            res = 0
        return res
    
    b, d = map(int, sys.stdin.readline().split())
    
    a = sys.stdin.readline().split()[0]
    c = sys.stdin.readline().split()[0]
    
    if False:
        b, d = 841, 7
        a = 'qjqhrksmvedtqldrqgchhsofokfcovut'
        c = 'qhtmothoulodshrfejterjlguvooccsvqrrdfqfvkqhtecuhhuqhshthrkusrc'
    
        b, d = 10,3
        a = 'abab'
        c = 'bab'
    
    
    
    
    print solve(a, b, c, d)