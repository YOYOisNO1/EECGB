    import sys
    debug = False
def solve(a, b, c, d):
        for i in c:
            if i not in a:
                return 0
        #w=[a,b]
        #q=[c,d]
        #[q,p] in w
        #p?
        ind1 = 0
        ind2 = 0
        cnt1 = 1
        cnt2 = 0
        phases = []
        phases2 = []
        
        while True:
            if a[ind1] == c[ind2]:
                ind2 += 1
                if ind2 == len(c):
                    #word finished!
                    cnt2 += 1
                    ind2 = 0
                    #check phase
                    if ind1 in phases:
                        #period!
                        cnt1_, cnt2_ = phases2[phases.index(ind1)]
                        step1 = cnt1 - cnt1_
                        step2 = cnt2 - cnt2_
                        cnt = (b-cnt1)/step1
                        cnt1 += step1 * cnt
                        cnt2 += step2 * cnt
                        phases = []
                        phases2 = []
                    #save phase
                    phases.append(ind1)
                    phases2.append([cnt1, cnt2])
    
            ind1 += 1
            if ind1 == len(a):
                cnt1 += 1
                ind1 = 0
                if cnt1 > b:
                    return cnt2 / d
        #answ  
        val2 = phases2[-1]
        val1 = phases2[phases.index(ind1)]
    
        step1 = val2[0] - val1[0]
        step2 = val2[1] - val1[1]
        
        if debug:
            print str(val1[0]) + " -- > " + str(val1[1])
            print str(val2[0]) + " -- > " + str(val2[1])
    
        res = step2 * b / (step1 * d)
        res = (b - val2[0]) * step2 / (step1 * d) + val2[1]
        if res < 0:
            return 0
        else:
            return res
    
    if not debug:
        b, d = map(int, sys.stdin.readline().split())
        
        a = sys.stdin.readline().split()[0]
        c = sys.stdin.readline().split()[0]
        print str(solve(a, b, c, d))
    else:
        vals = []
        vals.append([841, 7, 'qjqhrksmvedtqldrqgchhsofokfcovut' ,'qhtmothoulodshrfejterjlguvooccsvqrrdfqfvkqhtecuhhuqhshthrkusrc', 5])
        vals.append([933, 5, 'abaabdcbbabacbdddadbbb', 'babbadbaaadbbbbaabbaabccbbdbadbbbbbbdbcbdbaaadbdbdbbbbdcbbdcbdaadbd', 15])
        vals.append([875, 10, 'hjeaiemqfliohlicmhndhbfdmlmcnjjgbg', 'hojqhmbgjlfmlliimlhahfeihgmhhhnbmebhgnfhgmhfjqhmlnnddgmqldelnhebi', 4])
        vals.append([320672, 1, 'wyyojuothwmlvrglfzdzdbtubxuoffvncrswsaznmoijoi', 'ttvlvzxcvczuagwzgbfuwmmt', 40084])
        vals.append([5608475, 1, 'gbagadghfaedhddefgbehbbdedefbaaeddachgebhbcgahfdchffhbhfahhdegdhdfbccgefhcdhhcdfgdgfhcdffaacch', 'fgfadaaecdgabeahcacadcbfhhe', 1869491])
        vals.append([1263204, 1, 'dcbabceabbaebddaaecbddaceaedacddadadcbbadbdccdecdacdcaadbceeddccbceaade', 'abddbccbdca', 1894805])
        vals.append([100, 1, 'bca', 'abc', 99])
        vals.append([541, 9, 'bxhwcmunbdxcatppdsw', 'shbppncwbnsxxnxunwsbncpdchcbcspdcppdchmbbcuapphpdxbpcswcxpxpdscxpddbcppdxhpxbuxxdbpdpuudb', 1])
        vals.append([9447267, 1, 'cbdcbdbcdacbcabddbaabcbacbabcaacbabaccddcbbdbbaddcbcbaaadc', 'bbbbdbcbbbdbdbcdcacccbdcadadbacbcccc', 4723633])
        vals.append([1181362, 3, 'fckmaalkicfakhcbiglkekajmadjkj', 'zfkjkjgkmjhfkackkhhjalgkkclcklabggk', 0])
        for val in vals:
            b, d, a, c, answer = val
            res = solve(a, b, c, d)
            if res == answer:
                print '++++++++++++++++++++++++++++'
                pass
            else:
                print '----------------------------'
                print val
                print res
                print '----------------------------'
                sys.stdin.readline()
    