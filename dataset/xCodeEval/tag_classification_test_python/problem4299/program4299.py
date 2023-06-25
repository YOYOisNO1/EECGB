def program4299():
    s=input()
    k=int(input())
    c=0
    t1=0
    t2=0
    for i in range(0,len(s)):
        if(s[i]!='*' and s[i]!='?'):
            c=c+1
        elif(s[i]=='*'):
            t2=t2+1
        else:
            t1=t1+1
    if(c!=k):
        if(c<k and t2==0):
            print('Impossible')
        elif(c>k and c-t2-t1>k):
            print('Impossible')
        else:
            if(c<k):
                S=''
                temp=0
                for i in range(0,len(s)):
                    if(s[i]!='*' and s[i]!='?'):
                        S=S+s[i]
                    if(s[i]=='*' and temp==0):
                        S=S+S[-1]*(k-c)
                        temp=1
                print(S)
            else:
                diff=c-k
                S=''
                for i in range(0,len(s)):
                    if(s[i]!='*' and s[i]!='?'):
                        S=S+s[i]
                    else:
                        if(diff>0):
                            S=S[:len(S)-1]
                            diff=diff-1
                print(S)
                
    else:
        S=''
        for i in range(0,len(s)):
            if(s[i]!='*' and s[i]!='?'):
                S=S+s[i]
        print(S)
        