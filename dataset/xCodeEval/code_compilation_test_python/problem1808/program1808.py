def program1808():
    #include<bits/stdc++.h>
    #define MOD 1000000007
    #define MAX 100003
    using namespace std;
    using ll = long double;
    
    int main(){
    	int t;
    	cin>>t;
    	while(t--){
    		int n ;
    		cin>>n;
    		ll ar[n];
    		for( int i = 0; i<n; i++){
    			cin>>ar[i];
    		}
    		sort(ar, ar+n );
    		for(int i = n-1; i>0; i--){
    			ar[i-1] = ( ar[i] + ar[i-1])/2.0;
    		}
    		cout<<ar[0]<<endl;
    	}
    }
    		