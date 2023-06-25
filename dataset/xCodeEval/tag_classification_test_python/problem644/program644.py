def program644():
    n=input()
    #25
    if('2' not in n or '5' not in n):a=10**18
    else:
        a=0
        i=len(n)-1
        while n[i]!='5':
            i-=1
            a+=1
        updated_n=n[0:i]+n[i+1:]
        i=len(n)-2
        while updated_n[i]!='2':
            i-=1
            a+=1
        updated_n=updated_n[0:i]+updated_n[i+1:]
        for i in range(len(updated_n)):
            if(updated_n[i]!='0'):
                break
        a+=i    
    #75
    if('7' not in n or '5' not in n):b=10**18
    else:
        b=0
        i=len(n)-1
        while n[i]!='5':
            i-=1
            b+=1
        updated_n=n[0:i]+n[i+1:]
        i=len(n)-2
        while updated_n[i]!='7':
            i-=1
            b+=1
        updated_n=updated_n[0:i]+updated_n[i+1:]
        for i in range(len(updated_n)):
            if(updated_n[i]!='0'):
                break
        b+=i        
    #50
    if('5' not in n or '0' not in n):c=10**18
    else:
        c=0
        i=len(n)-1
        while n[i]!='0':
            i-=1
            c+=1
        updated_n=n[0:i]+n[i+1:]
        i=len(n)-2
        while updated_n[i]!='5':
            i-=1
            c+=1
        updated_n=updated_n[0:i]+updated_n[i+1:]
        for i in range(len(updated_n)):
            if(updated_n[i]!='0'):
                break
        c+=i        
    #00
    if(n.count('0')<2):d=10**18
    else:
        d=0
        i=len(n)-1
        while n[i]!='0':
            i-=1
            d+=1
        updated_n=n[0:i]+n[i+1:]
        i=len(n)-2
        while updated_n[i]!='0':
            i-=1
            d+=1
        updated_n=updated_n[0:i]+updated_n[i+1:]
        for i in range(len(updated_n)):
            if(updated_n[i]!='0'):
                break
        d+=i        
    ans=min(a,b,c,d)
    if(ans==10**18):print(-1)
    else:print(ans)