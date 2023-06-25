def f(start,ends_with):
        n1=len(start)
        n2=len(ends_with)
        ans=""
        if(int(start[n1-n2:])<int(ends_with)):
            ans=start[0:n1-n2]+ends_with
        else:
            if n1==n2:
                temp=int(start[0:n1-n2]+'0')
            else:
                temp=int(start[0:n1-n2])
            temp+=1
            ans=str(temp)+ends_with
        return ans
    n=input()
    for kk in range(0,n):
        s=input()[4:]
        l=len(s)
        temp="1988"
        for i in range(l-1,-1,-1):
            temp=f(temp,s[i:])
        print temp