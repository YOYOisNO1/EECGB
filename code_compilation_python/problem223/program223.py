def function(x,y,m,c):
        d=y+x/m-c
        return d
def pval(a):
        return a[0]+a[1]
def valof(a,p):
        max=0
        for i,j in p:
            if j<=a:
                sum=0
                for l,m in p:
                    if m<=j and l<=i:sum+=l+m
                if max<=sum:max=sum#;print((i,j),sum)
        return max
    
    m,c=list(map(int,input().split()))
    p=[(i,j) for i in range(0,m*c+1) for j in range(0,c+1) if function(i,j,m,c)<=0]
    print(valof(c,p))
    
    