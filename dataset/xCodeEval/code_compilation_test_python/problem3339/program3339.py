def program3339():
    #include<bits/stdc++.h>
    using namespace std;
    int main(){
      ios_base::sync_with_stdio(false);
      cin.tie(NULL);cout.tie(NULL);
      int n,a=0,b=0,k=1,p,m;
      char x;
      cin>>n;
      m=n/2;
      for(int i=0;i<n;i++){
        cin>>x;
        p=int(x)-48;
        if(p!=4 && p!=7){k=0;}
        if(i<m){a+=p;}
        else{b+=p;}
      }
      if(k && a==b){cout<<"YES";}
      else{cout<<"NO";}
    }