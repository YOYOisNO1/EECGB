def program2358():
    #include<bits/stdc++.h>
    using namespace std;
    int main()
    {
        int x,y;
        cin>>x>>y;
        if(log(x)*y/log(y)*x) puts(">");
        else if(log(x)*y/log(y)*x) puts("<");
        else puts("=");
    }