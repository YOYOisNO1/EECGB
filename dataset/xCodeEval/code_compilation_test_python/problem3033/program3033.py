    s = input()
    k = input()
    k1 = ''
    for i in range(k):
        k1 += '1'
    s = s + k1
    
def sravn(s):
        for i in xrange(len(s)/2):
            if s[i] != s[i+len(s)/2] and s[i+len(s)/2] != '1':
                return 'no'
            return 'yes'
    
    l = len(s)/2*2
    while l >= 2:
        for i in range(len(s)-l+1):
            t = sravn(s[i:l])
            if t == 'yes':
                print l
            else:
                l -= 2