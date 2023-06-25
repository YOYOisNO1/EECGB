def program3882():
    #include<bits/stdc++.h>
    
    using namespace std;
    
    int main(){
        long long a,b,m,n,i,res;
        cin>>a>>b>>n>>m;
        double temp = __gcd(m,n);
        double j =m/(1.0*temp);
        double k =n/(1.0*temp);
        if (j/(1.0*k)<=b/(1.0*a)) cout<<int(a/(1.0*k))<<endl;
        else cout<<int((k/j)*b/k)<<endl;
     
        return 0;
    }