def program4447():
    s=list(input())
    i=1
    c=0
    while i<len(s)-3:
        if s[i]+s[i+1]+s[i+2]=='dot':
            s[i]='.'
            s[i+1]=''
            s[i+2]=''
            i+=1
        elif s[i]=='a' and s[i+1]=='t' and c==0:
            s[i]='@'
            s[i+1]=''
            c=1
        i+=1
    if s[i]=='a' and s[i+1]=='t' and c==0:
            s[i]='@'
            s[i+1]=''        
    #print(s)
    print(''.join(s))        