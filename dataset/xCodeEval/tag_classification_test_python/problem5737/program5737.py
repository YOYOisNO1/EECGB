    a,b,k=map(int, input().split())
def c(a,b,k):
        return a*k/b+(a*k%b > (b+1)/2)
def d(a,b,x,y):
        return abs(((a*y-b*x)*1.)/(b*y))
    
    m=min((d(a,b,c(a,b,i),i), i, c(a,b,i)) for i in range(1,k+1))
    print("%s/%s")%(m[2],m[1])