def program1684():
    n=int(input())
    s=input()
    a=[]
    for i in range(n):
        a.append(ord(s[i]))
    visit=[0 for i in range(n)]
    i,flag=1,0
    rama=[0 for i in range(n)]
    while(i<n):
        if(a[i]<a[i-1]):
            visit[i]=1
            rama[i]=visit[i]
        temp=a[i]
        tempu=visit[i]
        j=i
        while(j>0):
            if(temp<a[j-1]):
                if(tempu!=visit[j-1]):
                    a[j]=a[j-1]
                    visit[j]=visit[j-1]
                else:
                    flag=-1
                    break
            else:
                break
    
            j-=1
        if (flag==-1):
            break
        visit[j]=tempu
        a[j]=temp
    
        i+=1
    if(flag==-1):
        print("NO")
    else:
        print("YES")
        for i in rama:
            print(i,end='')