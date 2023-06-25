def program1389():
    #include <bits/stdc++.h>
    using namespace std;
    typedef long long ll;
    #define F first
    #define S second
    #define pb push_back
    int n;
    string ans;
    char track_two[1001][1001],track_five[1001][1001];
    int two[1001][1001],five[1001][1001];
    void solve(int arr[][1001],char track[][1001]){
    	for(int i=1;i<n;i++)
    	for(int j=1;j<n;j++){
    		if (arr[i][j-1]<arr[i-1][j]){
    			track[i][j] = 'R';
    			arr[i][j] += arr[i][j-1];
    			}
    		else{
    			track[i][j] = 'D';
    			arr[i][j] += arr[i-1][j];
    		}}
    	}
    
    void result(char track[][1001]){
    	int i=n-1,j=n-1;
    		while(i!=0 or j!=0){
    			if (track[i][j]=='D'){
    				ans += 'D';
    				i-=1;
    				}
    			else ans += 'R',j-=1;
    			}
    	}
    int main(){
    	cin>>n;
    	bool zero=false;
    	pair<int,int> zeroval;
    	
    	for(int i=0;i<n;i++)
    	for(int j=0;j<n;j++){
    		int a;
    		cin>>a;
    		if (a==0){a = 10,zero = true,zeroval={i,j};}
    		int cnt=0;
    		while(a%2==0) cnt++,a/=2;
    		two[i][j] = cnt;
    		cnt = 0;
    		while(a%5==0) cnt++,a/=5;
    		five[i][j] = cnt;
    		}
    	for(int i=1;i<n;i++){
    		two[0][i]+=two[0][i-1];
    		track_two[0][i] = 'R';
    		two[i][0]+=two[i-1][0];
    		track_two[i][0] = 'D';
    		five[i][0]+=five[i-1][0];
    		track_five[0][i] = 'R';
    		five[0][i]+=five[0][i-1];
    		track_five[i][0] = 'D';
    		}
    	solve(two,track_two);
    	solve(five,track_five);
    	if (zero){
    		if (two[n-1][n-1]!=0 and five[n-1][n-1]!=0){ cout<<1<<'\n';
    		int i=0,j=0;
    		while(i!=zeroval.F) cout<<'D',i++;
    		while(j!=zeroval.S) cout<<'R',j++;
    		while(i!=n-1) cout<<'D',i++;
    		while(j!=n-1) cout<<'R',j++;
    		exit(0);
    		}
    		}
    	//cout<<two[n-1][n-1]<<' '<<five[n-1][n-1];
    	//result(track_two);
    	//reverse(ans.begin(),ans.end());
    	//cout<<ans;
    	//for(auto i:track_two)
    	//for(int j=0;j<n;j++) cout<<i[j]<<' ';
    	if (two[n-1][n-1]<five[n-1][n-1]){
    		cout<<two[n-1][n-1]<<'\n';
    		result(track_two);
    		}
    	else cout<<five[n-1][n-1]<<'\n',result(track_five);
    	reverse(ans.begin(),ans.end());
    	cout<<ans<<'\n';
    	}