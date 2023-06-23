def program2844():
    #include <bits/stdc++.h>
    using namespace std;
    
    int main(){
      string n; int q=0;
      cin >> n;
      int strlen = n.size()*2/(round(sqrt(n.size()))+1);
      for (int i=1; i<strlen+1; i++){
        cout << n[q];
        q+=i;
      }
    }