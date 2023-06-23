def program1623():
    /*
     * Competetive Programming
     * Navya Aggarwal
     * iamnavya_agg
     */
    
    #include <bits/stdc++.h>
    
    using namespace std;
    
    int gcd(int a, int b)
    {
        if (a==0)
            return b;
        return gcd(b%a,a);
    }
    
    int lcm(int a, int b)  
    {  
        return (a*b)/gcd(a, b);
    }
    
    void func()
    {
        int n,m;
        cin>>n;
        cin>>m;
        std::vector<string> mat(n);
        for(int i=0; i<n; i++)
        {
            cin>>mat[i];
        }
        int count = 0;
        for(int i=0; i<n-1; i++)
        {
            if (mat[i].at(m-1) == 'R')
                count+=1;
        }
        for(int i=0; i<m-1; i++)
        {
            if (mat[n-1].at(i) == 'D')
                count+=1;
        }
        cout<<count<<endl;
    }
    
    int main()
    {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
        int t;
        cin>>t;
        for(int i=0; i<t; i++)
            func();
        return 0;
    }