    #908D
    n,a,b = map(int,input().split())
    
    p = 1000000007
    
def inv(a):
        p = 1000000007
        s=1
        n=p-2
        while n:
            if n&1:
                s=s*a%p
            a=a*a%p
            n/=2
        return s
    f=[[0 for i in range(1001)] for j in range(1001)]
    u=a*inv(a+b)%p
    v=(1-u+p)%p
    c=u*inv(v)%p
    for i in range(n,0,-1):
        for j in range(n-1,-1,-1):
            if j+i>=n:
                f[i][j]=(j+i+c)%p
            else:
                f[i][j]=(u*f[i+1][j]+v*f[i][j+i])%p
    print f[1][0]
    
    """
    #include<cstdio>
    typedef long long ll;
    const int p=1e9+7;
    ll inv(ll a){
    	ll s=1;
    	for(int n=p-2;n;n>>=1){
    		if(n&1)s=s*a%p;
    		a=a*a%p;
    	}
    	return s;
    }
    int n,a,b,f[1001][1001];
    int main(){
    	scanf("%d%d%d",&n,&a,&b);
    	ll u=a*inv(a+b)%p,v=(1-u+p)%p,c=u*inv(v)%p;
    	for(int i=n;i;--i)
    		for(int j=n-1;~j;--j)
    			f[i][j]=(j+i>=n?j+i+c:u*f[i+1][j]+v*f[i][j+i])%p;
    	printf("%d\n",f[1][0]);
    }
    """