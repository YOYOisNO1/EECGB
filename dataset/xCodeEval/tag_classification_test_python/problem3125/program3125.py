def program3125():
    m,s=map(int,input().split(" "))
    np=m
    if m==1 and s==0:
        print('0 0')
    elif m==0 or s>(9*m) or s==0:
        print('-1 -1')
    else:
        st,stmin='',''
        j=s
        while(j>9):
            st='9'+st
            stmin=stmin+'9'
            j=j-9
            np-=1
        st=st+(str)(j)+'0'*(np-1)
        if np==1:
            stmin=(str)(j)+stmin
        else:
            stmin='1'+(np-2)*'0'+(str)(j-1)+stmin
        print(stmin,)
        print(st)
        