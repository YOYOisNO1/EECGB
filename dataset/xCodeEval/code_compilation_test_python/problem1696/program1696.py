def program1696():
    #include<cstdio>
    
    int main()
    {
        int n, m, k, c[16]={0}, ans=0;
        scanf("%d%d%d", &n, &m, &k);
        
        for(int i=0; i<n; i++)
        {
            char s[16], cnt=0;
            scanf("%s", s);
            
            for(int j=0; j<m; j++)
                if( s[j]=='Y' )
                    cnt++;
            
            if( cnt>=k )
                ans++;
        }
        
        printf("%d\n", ans);
    }