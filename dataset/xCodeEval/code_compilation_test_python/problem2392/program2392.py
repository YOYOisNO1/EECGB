def program2392():
    #include<stdio.h>
    #include<string>
    #include<math.h>
    #include<stdlib.h>
    #include<set>
    #include<bitset>
    #include<map>
    #include<vector>
    #include<string.h>
    #include<algorithm>
    #include<iostream>
    #include<queue>
    #include<deque>
    #include<stack>
    #include<cmath>
    #include<ctime>
    #include<complex>
    using namespace std;
    
    string a,b;
    int num[10];
    
    void print(){
    	for(int i=9;i>=0;i--) while(num[i]){
    		num[i]--;
    		cout<<i;
    	}
    	exit(0);
    }
    
    int main(){
    	cin>>a>>b;
    	for(int i=0;i<a.size();i++) num[a[i]-'0']++;
    	if(a.size()<b.size()) print();
    	for(int i=0;i<a.size();i++){
    		int x=b[i]-'0';
    		int j=x;
    		for(j=x;j>=0;j--) if(num[j]) break;
    		num[j]--;
    		cout<<j;
    		if(j!=x){
    			print();
    			break;
    		}
    	}
    	return 0;
    }