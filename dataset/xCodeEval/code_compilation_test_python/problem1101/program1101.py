def program1101():
    #include<bits/stdc++.h>
    #define rep(i,n) for(int i=0;i<n;i++)
    #define rep1(i,n) for(int i=n-1;i>=0;i--)
    #define range(i,p,q) for(int i=p;i<=q;i++)
    #define pb push_back
    #define fi first
    #define se second
    #define mp make_pair
    #define io ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    typedef long long ll;
    using namespace std;
    int main(){
    	io
    	int n,a,b;
    	cin>>n;
    	a=(n%2)?n/2:n/2-1;
    	b=n-a;
    	//cout<<a<<" "<<b<<endl;
    	while(__gcd(a,b)!=1) a--,b++;
    	cout<<a<<" "<<b;
    }