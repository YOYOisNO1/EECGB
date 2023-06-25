def program382():
    s=input()
    ln=len(s)
    cnt1=0
    cnt2=0
    cnt3=0
    for i in range(0,ln):
        if(s[i]=='a'):
            cnt1+=1
        elif(s[i]!='a'):
            cnt2+=1
    if(cnt1>cnt2 and cnt1>(ln/2)):
        print(ln)
    elif(cnt1==cnt2):
        print(ln-1)
    else:
        while(1):
            cnt2-=1
            if(cnt1>cnt2):
                cnt3=1
                break
        if(cnt3==1):
            print(cnt1+cnt2)
            