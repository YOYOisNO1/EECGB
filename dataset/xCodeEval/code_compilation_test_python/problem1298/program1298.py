def program1298():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    #define ll long long
    
    
    int main(){
        int n;
        cin >> n;
    
        while(n--){
            int angle;
            cin >> angle;
    
            if(360 % (180 - angle) == 0) cout << "YES\n";
            else cout << "NO\n";
    
        }
    
    
    
        return 0;
    }