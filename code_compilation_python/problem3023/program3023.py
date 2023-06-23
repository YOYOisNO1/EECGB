    s=input()
    import math
def rec(s,lis):
        new=[]
        if(len(lis)!=0 and len(lis[0])==1):
            return -1
        elif(len(lis)==0):
            for i in range(len(s)):
                a=s[:i]+s[i+1:]
                if(math.sqrt(int(a))-int(math.sqrt(int(a)))==0 and a[0]!="0"):
                    return (len(s)-len(a))
                new.append(a)
        else:
            for j in range(len(lis)):
                k=lis[j]
                for i in range(len(k)):
                    a=k[:i]+k[i+1:]
                    if(math.sqrt(int(a))-int(math.sqrt(int(a)))==0 and a[0]!="0"):
                        return (len(s)-len(a))
                    new.append(a)
        return rec(s,list(set(new)))
    lis=[]
    if(math.sqrt(int(s))-int(math.sqrt(int(s)))==0 and s[0]!="0"):
        print(0)
    else:
        ans=rec(s,lis)
        print(ans)