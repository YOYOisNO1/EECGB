def program2506():
    #include <iostream>
    #include <bitset>
    #include <functional>
    #include <vector>
    #include <stdio.h>
    #include <string>
    #include <map>
    #include <set>
    #include <list>
    #include <climits>
    #include <algorithm>
    using namespace std;
    
    void solve(){
    	int n, m;
    	cin>>n>>m;
    	vector<pair<int, int>> arr(m);
    	for(auto &item : arr){
    		cin>>item.first>>item.second;
    	}
    	sort(arr.begin(), arr.end(), [](pair<int, int> a, pair<int, int> b){
    		if(a.second<b.second)return true;
    		return false;
    	});
    	long long total=0;
    	while(n>0){
    		total+=arr.back().second*min(n, arr.back().first);
    		n-=min(n, arr.back().first);
    		arr.pop_back();
    	}
    	cout<<total<<endl;
    }
    
    int main(){
    	int t=1;
    //	cin>>t;
    	while(t--){
    		solve();
    	}
    	
    }