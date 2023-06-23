def program1645():
    #include <bits/stdc++.h>
    using namespace std;
    
    #define ll long long
    
    int main()
    {
    	char a[],b[];
    	cin>>a>>b;
    	vector<char> tot;
    	tot.push_back(a[0]);
    	for(ll i=1;i<a.length();i++){
    		if(a[i]<b[0]){
    			tot.push_back(a[i]);
    		}
    		else{
    			tot.push_back(b[0]);
    			break;
    		}
    	}
    	cout<<tot<<endl;
    	return 0;
    }