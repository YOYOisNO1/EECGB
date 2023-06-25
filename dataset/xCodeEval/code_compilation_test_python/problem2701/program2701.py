def program2701():
    #include <iostream>
    #include <vector>
    using namespace std;
    
    int a, b;
    int main() {
        cin >> a >> b;
        vector<int> v;
        int ok = 1;
        while (b > a) {
            //cout << b << endl;
            v.push_back(b);
            if ((b & 1) == 0) {
                b = b / 2;
            }
            else if (b % 10 == 1) {
                b = b / 10;
            }
            else { ok = 0; break;}
        }
    
        if (b != a) ok = 0; 
        else v.push_back(a);
    
    
        if (!ok) cout << "NO" << endl;
        else {
            cout << "YES" << endl;
            cout << v.size() << endl;
            for (int i = v.size()-1; i >0; i--)
                cout << v[i] << " ";
            cout << v[0] << endl;
        }
        return 0;
    }