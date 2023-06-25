def program1955():
    #include<iostream>
    #include<string>
    using namespace std;
    int main()
    {
        int n,k,inp,cur=0,i,ans=-1;
        cin>>n>>k;
        for(i=1;i<=n;i++)
        {
            cin>>inp;
            cur+=inp;
            if(cur<=8)
            {
                k-=cur;
                cur=0;
            }
            else
            {
                cur-=8;
                k-=8;
            }
            if(k<=0&&ans==-1)
                ans=i;
        }
        cout<<ans;
        return 0;
    }