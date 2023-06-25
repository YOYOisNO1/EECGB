def ans(s):
        sum=0
        for i in range(0,len(s),1):
            c=s[i]
            if(c.isupper()):
                sum+=1
        return sum
    
    s=str(input())
    l=len(s)
    x=''
    for i in range(0,l,1):
        if(s[i]=='>'):
            x+='1000'
        elif(s[i]=='<'):
            x+='1001'
        elif(s[i]=='+'):
            x+='1010'
        elif(s[i]=='-'):
            x+='1011'
        elif(s[i]=='.'):
            x+='1100'
        elif(s[i]==','):
            x+='1101'
        elif(s[i]=='['):
            x+='1110'
        elif(s[i]==']'):
            x+='1111'
    f=int(x,2)
    print(f%1000003)
            