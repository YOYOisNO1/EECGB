    n=int(input())
    mat=list(map(int,input().split()))
def gcd(a,b):
        if b==0:
            return a
        else:
            return gcd(b,a%b)
    k=gcd(mat[0],mat[1])
    for i in range(2,len(mat)):
        k=gcd(k,mat[i])
    print(k*n)