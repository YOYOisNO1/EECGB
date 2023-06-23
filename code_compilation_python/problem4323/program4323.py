    n=input()
def s(x):
        t=0
        while x :
            t+=x%10
            x/=10
        return t
    for i in range(1,int(n**0.5)+1):
        if i*i+s(i)*i == n :
            print i
            exit()
    print -1