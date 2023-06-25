def program4129():
    s=input()
    n=len(s)
    cnt,i=0,0
    ans=""
    if(s[0]=='9'):
        ans+='9'
        i+=1
    for j in range(i,n):
        ans+=str(min(int(s[j]),9-int(s[j])))
    print(ans)