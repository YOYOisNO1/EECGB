def program2559():
    #include <bits/stdc++.h>
    using namespace std;
    #define sfi ({register int x;scanf("%d",&x);x;})
    long long pw1(int p)
    {
        long long r=1;
        for(int i=1;i<=p;i++)
        {
            r*=10;
        }
        return r;
    }
    long long pw2(long long n,int j)
    {
        long long r=1;
        for(int i=0;i<j;i++)
        {
            r*=n;
        }
        return r;
    }
    int main()
    {
        int n=sfi;
        string s;
        cin>>s;
        reverse(s.begin(),s.end());
        /**
        create biggest number from smallest value digit to biggest value digit
        if found '0' then count it for next digit
        */
        long long num=0,cnt0=0,res=0,j=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='0')
            {
                cnt0++;
            }
            else
            {
                int p= (int(log10(num))+1)   +cnt0; ///total previous digit
                long long x=pw1(p)*(s[i]-48);       /// (present digit + trailing zero) number like 30000
                if(num+x>=n)          /// generated number till present digit
                {
                    //cout<<num<<endl;
                    res+=num*pw2(n,j);
                    num=0;
                    num=(s[i]-48)*pw1(cnt0);
                    j++;
                }
                else
                {
                    num+=x;
                }
                cnt0=0;
            }
        }
        //cout<<"---"<<num<<endl;
        if(num>=n)
        {
            j++;
            res+=(s[s.size()-1]-48)*pw2(n,j);
        }
        else res+=num*pw2(n,j);
    
        cout<<res;
    }