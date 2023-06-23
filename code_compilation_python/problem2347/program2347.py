def program2347():
    #include<bits/stdc++.h>
    using namespace std;
    int main(){
    	int n,m,j,k,i=0,l;
    	string s1,s2,s3;
    	cin>>s1>>s2;
    	while(1){
    		i++;
    		if(s1.empty()==true)break;
    		if(s1[i]<=s2[i]){
    			s3[i]=s1[i]-1;
    		}
    		else {
    			cout<<-1;
    			return 0;
    		}
    	}
    	cout<<s3;
    }