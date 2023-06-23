def program1165():
    //
    //  main.cpp
    //  D. Rat Kwesh and Cheese
    //
    //  Created by Dhruv Mullick on 01/02/16.
    //  Copyright © 2016 Dhruv Mullick. All rights reserved.
    //
    
    #include <bits/stdc++.h>
    
    using namespace std;
    
    #define ll long long
    #define ull unsigned long long
    #define pb push_back
    #define f first
    #define s second
    #define PI 3.14159265359
    typedef pair<int,int> ii;
    typedef pair<int,pair<int,int> > iii;
    
    string str[]={"x^y^z","x^z^y","(x^y)^z","(x^z)^y","y^x^z","y^z^x","(y^x)^z","(y^z)^x","z^x^y","z^y^x","(z^x)^y","(z^y)^x"};
    
    void findmax(double x, double y, double z)
    {
        double ans=0;
        double t=0;
        double eps=1e-10;
        int idx=0;
        if(x>1)
        {
            t=log(log(x))+z*log(y);
            if(t>ans+eps)
            {
                ans=t;
                idx=0;
            }
            t=log(log(x))+y*log(z);
            if(t>ans+eps)
            {
                ans=t;
                idx=1;
            }
            t=y*log(log(x))+log(z);
            if(t>ans+eps)
            {
                ans=t;
                idx=2;
            }
            t=z*log(log(x))+log(y);
            if(t>ans+eps)
            {
                ans=t;
                idx=3;
            }
        }
        else if(x==1)
        {
            t=1;
            if(t>ans+eps)
            {
                ans=t;
                idx=0;
            }
        }
        
        if(y>1)
        {
            t=log(log(y))+z*log(x);
            if(t>ans+eps)
            {
                ans=t;
                idx=4;
            }
            t=log(log(y))+x*log(z);
            if(t>ans+eps)
            {
                ans=t;
                idx=5;
            }
            t=x*log(log(y))+log(z);
            if(t>ans+eps)
            {
                ans=t;
                idx=6;
            }
            t=z*log(log(y))+log(x);
            if(t>ans+eps)
            {
                ans=t;
                idx=7;
            }
        }
        else if(y==1)
        {
            t=1;
            if(t>ans+eps)
            {
                ans=t;
                idx=4;
            }
        }
        
        if(z>1)
        {
            t=log(log(z))+y*log(x);
            if(t>ans+eps)
            {
                ans=t;
                idx=8;
            }
            t=log(log(z))+x*log(y);
            if(t>ans+eps)
            {
                ans=t;
                idx=9;
            }
            t=x*log(log(z))+log(y);
            if(t>ans+eps)
            {
                ans=t;
                idx=10;
            }
            t=y*log(log(z))+log(x);
            if(t>ans+eps)
            {
                ans=t;
                idx=11;
            }
        }
        else if(z==1)
        {
            t=1;
            if(t>ans+eps)
            {
                ans=t;
                idx=8;
            }
        }
        
        cout<<str[idx];
        
    }
    
    int main(int argc, const char * argv[])
    {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
        double x,y,z;
        double ans[12];
        double val;
        int i;
        cin>>x>>y>>z;
        
        if(x<1 && y<1 && z<1)
        {
            ans[0]=pow(x,pow(y,z));
            ans[1]=pow(x,pow(z,y));
            ans[2]=pow(x,y*z);
            ans[3]=pow(x,y*z);
            ans[4]=pow(y,pow(x,z));
            ans[5]=pow(y,pow(z,x));
            ans[6]=pow(y,z*x);
            ans[7]=pow(y,z*x);
            ans[8]=pow(z,pow(x,y));
            ans[9]=pow(z,pow(y,x));
            ans[10]=pow(z,y*x);
            ans[11]=pow(z,y*x);
            for(i=0;i<12;i++)
                val=max(val,ans[i]);
            for(i=0;i<12;i++)
                if(val==ans[i])
                    break;
            cout<<str[i];
        }
        else
            findmax(x,y,z);
        
        return 0;
    }