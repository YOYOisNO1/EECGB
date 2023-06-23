def program1798():
    #include <bits/stdc++.h>
    
    using namespace std;
    unsigned long long fact(long long n)
    {
        if(n==1) return 1;
        else return n*fact(n-1);
    }
    unsigned long long puissance (long long n,long long p)
    {
        unsigned long long i,s=1;
        for(i=0;i<p;i++)
            s=s*n;
        return s;
    }
    
    int main()
    {
    
        long long n,x,d;
        cin >>n;
        d=(puissance(10,9)+7);
        x=(puissance(3,3*n)-puissance(7,n))%d;
        cout << x;
        return 0;
    
    }