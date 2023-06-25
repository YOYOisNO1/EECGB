def program3209():
    n=input();i=0;j=len(n)-1;z=[]
    while(i<j):
        if n[i]=="(" and n[j]==")":z+=[[i+1,j+1]];i+=1;j-=1
        else:
            if n[i]==")":i+=1
            elif n[j]=="(":j-=1
    print(len(z))
    print(2*len(z))
    for i in z:print(i[0],end=" ")
    for i in z[::-1]:print(i[-1],end=" ")