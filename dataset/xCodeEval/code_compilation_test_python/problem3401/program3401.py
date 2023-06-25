def program3401():
    #include <iostream>
    #include <string>
    #include <vector>
    #include <map>
    #include <algorithm>
    #include <queue>
    #include <stack>
    #include <list>
    #include <cstring>
    #include <set>
    #include <climits>
    #include <math.h>
    #include <string>
    #include <functional>
    #include <numeric>
    
    #define int long long
    #define all(arr) begin(arr), end(arr)
    #define pb push_back
    #define em emplace_back
    
    using namespace std;
    signed main(){
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        int pos=-1;
        for(int i=0;i<n-1;i++){
            if(arr[i]<arr[i+1]){
                pos=i+1;
            }
        }
        cout<<"first "<<pos<<endl;
        while(pos+1<n and arr[pos]==arr[pos+1]){
            pos++;
        }
        cout<<pos<<endl;
        for(int i=pos;i<n-1;i++){
            if(arr[pos]>arr[pos+1])continue;
            cout<<pos<<endl;
            cout<<"NO"<<endl;
            return 0;
        }
        cout<<"YES"<<endl;
    }