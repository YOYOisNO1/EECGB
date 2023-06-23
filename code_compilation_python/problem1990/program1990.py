def program1990():
    #include <bits/stdc++.h>
    using namespace std;
    
    int main(){
        int a;
        cin >> a;
        set<int> s;
        int tmp;
        for ( int i = 0; i < a; i++ ){
            cin >> tmp;
            s.insert(tmp);
        }
        if( s.size() <= 2 ){
            cout << "NO\n";
            exit(0);
        }
        std::vector<int> v;
        for( auto x:s ){
            v.push_back(x);
        }
        for(int i = 0; i < v.size()-2; i++){
            if( v[i+2]-v[i] == 2 ){
                cout << "YES\n";
                exit(0);
            }
        }
        cout << "NO\n";
    }