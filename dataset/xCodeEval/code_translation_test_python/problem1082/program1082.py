def checkAP(s):
        d=s[1]-s[0]
        for i in range(len(s)-1):
            if(s[i+1]-s[i]!=d):
                return False
                break
        return True
    a=int(input())
    s=list(map(int,input().strip().split()))
    if(a==1):
        print(s[0])
    elif(a==2):
        print(s[1]+s[1]-s[0])
    else:
        if(checkAP(s)==True):
            print(s[0]+a*(s[1]-s[0]))
        else:
            print(s[a-1])