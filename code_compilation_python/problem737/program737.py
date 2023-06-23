def program737():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    long long pw(int power)
    {
        if (power==1) return 10;
        else return 10*pw(power-1);
    }
    
    int main()
    {
        int n;
        cin>>n;
        long long ans = 0;
        int power = 0;
        while(n>=10){
            power++;
            long long p=pw(power);
            n -= p - 1;
            ans +=  (p - 1) * power;
        }
        ans+=n*(power+1);
        cout<<ans;
        return 0;
    }