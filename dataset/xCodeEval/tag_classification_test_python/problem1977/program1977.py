def program1977():
    from collections import defaultdict as dd
    n,k=[int(i) for i in input().split()]
    if(n%2==0 and k>1):
        print('No')
    elif(n%2==0 and k==1):
        print('Yes')
    else:
        flag=0
        dic=dd(int)
        for i in range(1,k+1):
            if(dic[n%i]==1):
                flag=1
                break
            else:
                dic[n%i]=1
        if(flag==1):
            print('No')
        else:
            print('Yes')