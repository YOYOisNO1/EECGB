def program799():
    #include <string>
    #include <iostream>
    using namespace std;
    
    int main(){
        string s1, s2; char x;
        cin >> s1; cin.get(x); cin >> s2;
        reverse(s2.begin(), s2.end());
        if (s1 == s2) printf("YES");
        else printf("NO");
        return 0;
    }