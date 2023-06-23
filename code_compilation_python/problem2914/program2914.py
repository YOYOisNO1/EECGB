def program2914():
    #include<bits/stdc++.h>
    using namespace std;
    typedef long long ll;
    ll a[240000],b[240000],st[240000];
    int main() {
        ll T,n;
        scanf("%d",&T);
        while(T--) {
            scanf("%d",&n);
            if(n>=1&&n<=9)printf("%d\n",n);
            else if(n>=10&&n<=17)printf("%d9\n",n-9);
            else if(n>=18&&n<=24)printf("%d89\n",n-17);
            else if(n>=25&&n<=30)printf("%d789\n",n-24);
            else if(n>=31&&n<=35)printf("%d6789\n",n-30);
            else if(n>=36&&n<=39)printf("%d56789\n",n-35);
            else if(n>=40&&n<=42)printf("%d456789\n",n-39);
            else if(n>=43&&n<=44)printf("%d3456789\n",n-42);
            else printf("123456789\n");
        }
    }