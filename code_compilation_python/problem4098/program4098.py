def program4098():
    //============================================================================
    // Name        : A.cpp
    // Author      : 
    // Version     :
    // Copyright   : Your copyright notice
    // Description : Hello World in C++, Ansi-style
    //============================================================================
    
    #include <iostream>
    #include <string.h>
    #include <algorithm>
    #include <stdio.h>
    using namespace std;
    long long dp[20][12];
    int bit[20];
    long long dfs(int pos,int pre1,int pre2,bool flag,bool z)
    {
        if(pos==-1)return pre1==pre2;
        if(pre1!=0 && !flag &&dp[pos][pre1]!=-1)
            return dp[pos][pre1];
        long long ans=0;
        int end=flag?bit[pos]:9;
        for(int i=0;i<=end;i++)
        {
            ans+=dfs(pos-1,(z)?i:pre1,i,flag && i==end,z&&(i==0));
        }
        if(!flag &&pre1!=0)dp[pos][pre1]=ans;
        return ans;
    }
    long long calc(long long n)
    {
        int len=0;
        while(n)
        {
            bit[len++]=n%10;
            n/=10;
        }
        return dfs(len-1,0,0,1,1);
    }
    int main()
    {
        long long l,r;
        memset(dp,-1,sizeof(dp));
        while(scanf("%I64d%I64d",&l,&r)==2)
        {
            printf("%I64d\n",calc(r)-calc(l-1));
        }
        return 0;
    }