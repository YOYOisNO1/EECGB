def program3542():
    #include <bits/stdc++.h>
    
    using namespace std;
    struct s
    {
        int val,ind;
    };
    s arr[100003];
    bool cmp(s a,s b)
        return a.val<b.val;
    }
    int main()
    {
        int n,i;
        bool works;
        scanf("%d",&n);
        for (i=1;i<=n;i++)
        {
            scanf("%d",&arr[i].val);
            arr[i].ind=i;
        }
        sort(arr+1,arr+n+1,cmp);
        printf("%d\n",n/2+n%2);
        works=0;
        for (i=1;i<=n;i+=2)
        {
            if (!works) works=1;
            else printf(" ");
            printf("%d",arr[i].ind);
        }
        printf("\n");
        printf("%d\n",n/2);
        works=0;
        for (i=2;i<=n;i+=2)
        {
            if (!works) works=1;
            else printf(" ");
            printf("%d",arr[i].ind);
        }
        printf("\n");
        return 0;
    }