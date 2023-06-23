def program2500():
    s=input()
    new_s=s
    s=s.replace(' ','')
    
    a=[]
    for i in s:
        if i=='=':break
        a.append(i)
    
    
    l=len(a)-1
    i=s.index('=')+1
    s1=s[i:]
    if(l==len(s1)):
        print(new_s)
    
    elif(abs(l-len(s1))<=2):
        if l<len(s1):
            a.append('|')
            s1=list(s1)
            s1.remove('|')
            s1=''.join(s1)
    
        else:
            s1=list(s1)
            s1.append('|')
            a.remove('|')
            s1=''.join(s1)
    
        a=''.join(a)
        a1=[]
        for i in range(len(a)):
            try:
                if a[i]=='+' :
                    a1.append(' ')
                    a1.append(a[i])
                    a1.append(' ')
                else:a1.append(a[i])
    
    
    
    
            except:IndexError
        #print(a1)
        a1=''.join(a1)
        if len(a1)-3==len(s1):
    
            print(str(a1)+' = '+s1)
            
         else:print('Impossible')
    else:
        print('Impossible')
    
    
    
    
    
    
            
            
            
            