def program814():
    #include <iostream>
    
    using namespace std;
    int n,k;
    string s;
    int main()
    {
        cin >> n >> k;
        cin >> s;
        int cnt=0;
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                if (s[i]==s[j] and i!=j){
                    cnt+=1
                }
    
    
            }
            if (cnt>k){
            cout<<"NO";
            return 0;
            }
        }
        cout<<"YES";
        return 0;
    }