def program320():
    s=input()
    n=len(s)
    i=0
    st=""
    ls=[]
    while(i<n):
        if i<n-2 and (s[i],s[i+1],s[i+2])==('W','U','B'):
            i+=3
            ls.append(st)
            st=""
        else:
            st+=s[i]
            i+=1
    ls.append(st)
    for i in ls:print(i,end=" ")