def program1787():
    #include <bits/stdc++.h>
    using namespace std;
    #define For(i,a,b) for(int i=a;i<b;i++)
    #define mp make_pair
    #define pb push_back
    #define mod 1000000007
    
    long long h,n,ans;
    
    int main( ){
        //freopen("input.txt","r",stdin);
        ios::sync_with_stdio(0);
        cin>>h>>n;
        ans=0;
        n-=1;
        bool lef=true;
        while(h>0)
        {
            if((lef&& (n<(1ll<<(h-1))) )||( (!lef)&&n>=(1ll<<(h-1)) ) )
            {
                ans++;
                //if((~lef)&&n>=(1ll<<(h-1))) cout<<"ASDFASDF";
                //cout<<n<<' '<<(1ll<<(h-1))<<' ';
                lef=!lef;
                h--;
                n%=(1ll<<h);
                //cout<<(1ll<<(h-1))<<' ';
            }
            else
            {
                ans+=(1ll<<h);
                h--;
                n%=(1ll<<h);
            }
            //cout<<ans<<' '<<h<<endl;
        }
        cout<<ans;
        return 0;
    }