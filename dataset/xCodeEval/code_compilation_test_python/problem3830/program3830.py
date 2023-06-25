def program3830():
    #include <bits/stdc++.h>
    
    #define uint unsigned int
    #define INF 999999999
    #define LINF 999999999999999999
    #define ll long long
    #define M 100
    #define E 0.0000001
    #define N (1<<18)
    #define pii pair<int, int>
    #define pll pair<long long, long long>
    #define pdd pair<double, double>
    #define ull unsigned long long
    
    using namespace std;
    
    
    int main () {
        ll n;
        cin>>n;
        cout<<n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * n * (n - 1) * (n - 2) * (n - 3) * (n - 4)<<endl;
    }