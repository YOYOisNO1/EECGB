def program2007():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    int n;
    
    int main(){
       cin >> n;
       vector <int> v(n);
       for(int i = 0; i < n; i++) cin >> v[i];
       sort(v.begin(), v.end());
       for(int i = 0; i < n; i++)
          printf( i == n - 1 ? "%d\n" : "%d ", v[i]);
       return(0);
    }