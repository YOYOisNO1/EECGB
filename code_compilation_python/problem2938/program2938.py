def program2938():
    s=input()
    l=len(s)
    if l>=5:
        caps=0
        s=0
        n=0
        for i in s:
            if caps>0 and s>0 and n>0:
                break
            if i>='a' and i<='z':
                s=s+1
            elif i>='A' and i<='Z':
                caps=caps+1
            elif i>='0' and i<='9'
                n=n+1
        if A>0 and a>0 and n>0:
            print('Correct')
        else:
            print('Too weak')
    else:
        print('Too weak')