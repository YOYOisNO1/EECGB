def program2234():
    #include <bits/stdc++.h>
    #define F first
    #define S second
    #define mid ((l + r) / 2)
    #define lson (id * 2)
    #define rson (id * 2 + 1)
    using namespace std;
    typedef long long ll;
    const int maxn = 3e5 + 4;
    
    int a, b, c;
    int main(){
    	cin>>a>>b>>c;
    	a *= 10;
    	int cnt = 1;
    	while(cnt<=b){
    		while(a < b and cnt <= b){
    			a *= 10;
    			if(c==0){
    				cout<<cnt<<'\n';
    				exit(0);
    			}
    			cnt++;
    		}
    		int rem = a / b;
    		if(rem == c){
    			cout<<cnt<<'\n';
    			exit(0);
    		}
    		a = a % b;
    		a *= 10;
    		cnt++;
    	}
    	if(c == 0 and cnt!=b+1) cout<<cnt<<'\n';
    	else cout<<-1<<'\n';
    }