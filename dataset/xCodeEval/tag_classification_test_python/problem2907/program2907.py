def program2907():
    s=input()
    k={'R':0,'B':0,'Y':0,'G':0}
    flag=0
    ind={0:'R',1:'B',2:'Y',3:'G'}
    for i in xrange(0,len(s)):
        if s[i]!='!':
            ind[i%4]=s[i]
    for i in xrange(0,len(s)):
        if s[i]=='!':
            k[ind[i%4]]+=1
    print(k['R'],k['B'],k['Y'],k['G'])