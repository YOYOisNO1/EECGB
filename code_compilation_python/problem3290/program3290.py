def program3290():
    s=input()
    if(s[0]=='h'):
        s1 = s[:4]+'://'
        s2 = ''
        s =s[4:]
        if (s[0] == 'r' and s[1] == 'u'):
            s1 = s1 + s[0] +s[1]
            s=s[2:]
            for i in range(len(s)):
                if(s[i]=='r' and s[i+1]=='u'):
                    sm = s[:i]
                    s1 = s1+sm+'.ru'
                    s2 = s2 + s[i+2:]
                    break
            if(len(s2)>0):
                ans = s1+'/'+s2
            else:
                ans = s1+s2
            print(ans)
        else:
            for i in range(len(s)):
                if(s[i]=='r' and s[i+1]=='u' ):
                    sm =s[:i]
                    s1 = s1+sm+'.ru'
                    s2 = s2+s[i+2:]
                    break
            if(len(s2)>0):
                ans = s1+'/'+s2
            else:
                ans = s1+s2
            print(ans)
    elif(s[0]=='f'):
    
        s1 = s[:3]+'://'
        s2 = ''
        s =s[3:]
        if (s[0] == 'r' and s[1] == 'u'):
            s1 = s1 + s[0] +s[1]
        else:
            for i in range(len(s)):
                if(s[i]=='r' and s[i+1]=='u' ):
                    sm =s[:i]
                    s1 = s1+sm+'.ru'
                    s2 = s2+s[i+2:]
                    break
            if(len(s2)>0):
                ans = s1+'/'+s2
            else:
                ans = s1+s2
        print(ans)