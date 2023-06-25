def program3590():
    '''''''''''
       Author : code_marshal
    '''''''''''
    
    alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    k, s = int(input()), list(input())
    ch = alp[:k]
    j=len(s)//2
    i=len(s)//2-1
    while i>=0 or j<len(s):
        if s[i]=='?':
            if s[~i]!='?': s[i]=s[~i]
            else:
                lol = list(set(ch)-set(s)); lol.sort(reverse=True)            k = 0
                for l in lol:k=l; break
                if k==0: s[i]=s[~i]=ch[0]
                else: s[i]=s[~i]=k
                if '?' not in s: break
        if s[j]=='?':
            if s[~j]!='?': s[j]=s[~j]
            else:
                lol = list(set(ch)-set(s)); lol.sort(reverse=True)
                k = 0
                for l in lol:k=l; break
                if k==0: s[j]=s[~j]=ch[0]
                else: s[j]=s[~j]=k
                if '?' not in s: break
        i-=1;j+=1
     
    if s[::-1]==s and not set(ch)-set(s): print(''.join(s))
    else: print("IMPOSSIBLE")