def program3502():
    s1=input()
    s2=input()
    t1=s1.split(':')
    t2=s2.split(':')
    for i in range(len(t1)):
        t1[i]=int(t1[i])
        t2[i]=int(t2[i])
    time1=(t1[0]*60)+t1[1]
    time2=((t2[0]*60)+t2[1])
    dif=time2-time1
    hr,mn=0,0
    if(dif<120):
        hr=t1[0]
        mn=t1[1]+dif//2
       # print("1.hr=",hr," mn=",mn)
        if(mn>=60):
            hr=hr+(mn//60)
            mn=mn-(60*(mn//60))
       # print("1.new hr=",hr," mn=",mn)
    else:
        dif=dif//2
        newh=dif//60
        newmin=dif-(newh*60)
        hr=t1[0]+newh
        mn=t1[1]+newmin
        #print("2.hr=",hr," mn=",mn)
        if(mn>=60):
            hr=hr+(mn//60)
            mn=mn-(60*(mn//60))
       # print("2.new hr=",hr," mn=",mn)
    if(hr<10):
        ans='0'+str(hr)+':'
        if(mn<10):
            ans=ans+'0'+str(mn)
        else:
            ans=ans+str(mn)
    else:
        ans=str(hr)+':'
        if(mn<10):
            ans=ans+'0'+str(mn)
        else:
            ans=ans+str(mn)
    print(ans)
        