def program824():
    #include <bits/stdc++.h>
    using namespace std;
    int n,a,b,temp;
    int main(){
        cin>>n>>a>>b;
        bool arr[a];
        for(int i=0;i<a;i++){
            cin>>temp;
            arr[temp]=1;
        }
        for(int i=0;i<b;i++) cin>>temp;
        for(int i=1;i<=n;i++){
            if(arr[i]==1) cout<<1<<" ";
            else cout<<2<<" ";
        }
    }
    