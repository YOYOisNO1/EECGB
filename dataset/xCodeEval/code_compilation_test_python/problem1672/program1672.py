def program1672():
    #include<bits/stdc++.h>
    using namespace std;
    int n,m;
    int fail(int limit,int ar[])
    {
        int i;
        int sum=0;
      sort(ar,ar+n);
      for(i=limit;i>=0;i++)
      {
          sum=sum+ar[i];
         if(sum<=n)
            break;
      }
      return i;
    
    }
    int main()
    {
       int sum=0;
        cin>>n>>m;
        int ar[n],ar1[n];
        for(int i=0;i<n;i++){
            cin>>ar[i];
            ar1[i]=ar[i];
        }
        for(int i=0;i<n;i++)
        {
           // int ar1[i]=
            sum=sum+ar[i];
          if(sum<=m)
                cout<<0<<" ";
          else
          {
             cout<<fail(i-1,ar1)<<" ";
          }
        }
    }