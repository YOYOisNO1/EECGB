def program2779():
    #include <iostream>
    #include<stdio.h>
    #include<vector>
    using namespace std;
     
    int main()
    {
        int n,m=0,j=0;
        char str[1000];
        vector<char> v;
        cin>>n;
        cin>>str;
        for(int i=0;i<n;)
        {
            v.push_back(str[i]);
            j++;
            m++;
            i=i+m;
        }
        for(int i=0;i<v.size();i++)
        cout<<v[i];
        return 0;
    }