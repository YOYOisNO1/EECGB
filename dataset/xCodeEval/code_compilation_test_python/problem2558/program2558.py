def program2558():
    n=input('')
    k=input('')
    l=len(str(n))
    b=10**(n-1)
    a=[str(k)[-1]]
    k=str(k)
    k=k[::-1]
    k=k[1:]
    count=0
    for i in k:
        if int(i+a[count])<n and (i!='0' or len(a[count])<l):
            a[count]=str(i+a[count])
        else:
            a+=[i]
            count+=1
        if count>=1:
            for j in a[count-1][:len(a[count-1])-1]:
                if j=='0':
                    a[count]=a[count]+'0'
                else:
                    break
                
                    
    ans=0
    for i in range(len(a)):
        ans+=((n**i)*int(a[i]))
    print ans