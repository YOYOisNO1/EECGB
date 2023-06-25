def program614():
    n=int(input())
    a=list(input())
    c=[]
    flag=0
    for i in range(101):
        k = i
        flag=0
        for j in range(len(a)):
            if a[j]=='+':
                k+=1
            elif a[j]=='-' and k>0:
                k-=1
            else:
                flag=1
                break
        if flag==0:
            break
    print(k)