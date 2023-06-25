    n=input()
    a=input()
    a=list(a)
def fun():
        pre='2'
        for i in range(n):
            if a[i]=='1' and a[i]==pre:
                return False
            pre=a[i]
        return True
    f=fun()
    if f==0:
        print("No")
        exit()
    for i in range(n):
        if a[i]=='0':
            a[i]='1'
            t=fun()
            a[i]='0'
            if t==1:
                print("No")
                exit()
    print("Yes")
            