def program2632():
    #include <iostream>
    #include<cmath>
    using namespace std;
    
    int main()
    {
        int n,s;
        cin>>n;
        int ar[n];
        for(int i=0; i<n; i++)
            cin>>ar[i];
        
        
        for(int i=0; i<pow(2,n);i++)
        {
            int bac=i;
            s=0;
            for(int j=0; j<n; j++)
                if(bac%2==0)
                {
                    s-=ar[j];
                    bac/=2;
                }
                else
                {
                    s+=ar[j];
                    bac/=2;
                }
            if(s%360==0)
            {
                cout<<"YES";
                return 0;
            }
        }
        cout<<"NO";
        return 0;
    }