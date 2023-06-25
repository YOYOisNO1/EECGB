def program1476():
    
    #include <iostream>
    #include <algorithm>
    #include <list>
    #include <math.h>
    #include <set>
    #include <cstring>
    #include <map>
    #include <vector>
    #include <stack>
    
    using namespace std;
    typedef long long ll;
    typedef vector<ll> vi;
    typedef pair<ll,ll> ii;
    #define endl "\n"
    #define kn 300005
    #define md 1000000007
    #define x first
    #define y second
    #define pb push_back
    #define ms(i,a) memset(a,i,sizeof(a))
    #define f(i,a,b) for(int i=a;i<=b;i++)
    #define ff(i,x) for(int i=1;i<=x;i++)
    #define _ff(i,x) for(int i=x;i>=1;i--)
    #define _f(i,a,b) for(int i=b;i>=a;i--)
    #define ios ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    
    ll ans[kn],n,k,_[20];
    string s;
    
    int main() {
    	cin>>n>>k;
    	ll sum=0,ans=0,num=0;
    	_[0]=1;
    	ff(i,18) _[i]=_[i-1]*10;
    	while(sum<=k&&n>0&&ans<=18){
    		int tmp=(n%10) %9; if(tmp!=0) tmp++; 
    		//772346242764cout<<tmp<<endl;
    		sum+=tmp*_[ans];
    		//cout<<"hi "<<sum<<endl;
    		if(sum>k) break;
    		//cout<<"n: "<<n<<endl;
    		if(tmp>0) n-=tmp; 
    		n/=10;
    		ans++;
    		num++;
    	}
    	if(n) cout<<n;
    	ff(i,num) cout<<"9";
    }