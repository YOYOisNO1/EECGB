def program2068():
    #include<iostream>
    #include<algorithm>
    #include<vector>
    #include<stack>
    #include<queue>
    #include<map>
    #include<unordered_map>
    #include<string>
    #include<cstring>
    #include<cmath>
    #include<cstdio>
    const int N=1e5;
    const int mod=1e9+7;
    const int INF=0x7fffffff;
    const int inf=0x3f3f3f3f;
    using namespace std;
    int num[10];
    unsigned long long jc[20];
    unsigned long long ans=0;
    int i1,i2,i3,i4,i5,i6,i7,i8,i9,i0,tj=0;
    
    void tiao0y()
    {
        for(int i=1;i<=num[0];i++)
        {
            i0=i;
            if(!num[1] && !num[2] && !num[3] && !num[4] && !num[5] && !num[6] && !num[7] && !num[8] && !num[9]) ans+=1;
            else
            {
                if(i1>0) ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9+i0-1]/(max(jc[num[i1]-1],(unsigned long long)1)*max(jc[num[i2]],(unsigned long long)1)*max(jc[num[i3]],(unsigned long long)1)*max(jc[num[i4]],(unsigned long long)1)*max(jc[num[i5]],(unsigned long long)1)*max(jc[num[i6]],(unsigned long long)1)*max(jc[num[i7]],(unsigned long long)1)*max(jc[num[i8]],(unsigned long long)1)*max(jc[num[i9]],(unsigned long long)1));
                if(i2>0) ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9+i0-1]/(max(jc[num[i1]],(unsigned long long)1)*max(jc[num[i2]-1],(unsigned long long)1)*max(jc[num[i3]],(unsigned long long)1)*max(jc[num[i4]],(unsigned long long)1)*max(jc[num[i5]],(unsigned long long)1)*max(jc[num[i6]],(unsigned long long)1)*max(jc[num[i7]],(unsigned long long)1)*max(jc[num[i8]],(unsigned long long)1)*max(jc[num[i9]],(unsigned long long)1));
                if(i3>0) ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9+i0-1]/(max(jc[num[i1]],(unsigned long long)1)*max(jc[num[i2]],(unsigned long long)1)*max(jc[num[i3]-1],(unsigned long long)1)*max(jc[num[i4]],(unsigned long long)1)*max(jc[num[i5]],(unsigned long long)1)*max(jc[num[i6]],(unsigned long long)1)*max(jc[num[i7]],(unsigned long long)1)*max(jc[num[i8]],(unsigned long long)1)*max(jc[num[i9]],(unsigned long long)1));
                if(i4>0) ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9+i0-1]/(max(jc[num[i1]],(unsigned long long)1)*max(jc[num[i2]],(unsigned long long)1)*max(jc[num[i3]],(unsigned long long)1)*max(jc[num[i4]-1],(unsigned long long)1)*max(jc[num[i5]],(unsigned long long)1)*max(jc[num[i6]],(unsigned long long)1)*max(jc[num[i7]],(unsigned long long)1)*max(jc[num[i8]],(unsigned long long)1)*max(jc[num[i9]],(unsigned long long)1));
                if(i5>0) ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9+i0-1]/(max(jc[num[i1]],(unsigned long long)1)*max(jc[num[i2]],(unsigned long long)1)*max(jc[num[i3]],(unsigned long long)1)*max(jc[num[i4]],(unsigned long long)1)*max(jc[num[i5]-1],(unsigned long long)1)*max(jc[num[i6]],(unsigned long long)1)*max(jc[num[i7]],(unsigned long long)1)*max(jc[num[i8]],(unsigned long long)1)*max(jc[num[i9]],(unsigned long long)1));
                if(i6>0) ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9+i0-1]/(max(jc[num[i1]],(unsigned long long)1)*max(jc[num[i2]],(unsigned long long)1)*max(jc[num[i3]],(unsigned long long)1)*max(jc[num[i4]],(unsigned long long)1)*max(jc[num[i5]],(unsigned long long)1)*max(jc[num[i6]-1],(unsigned long long)1)*max(jc[num[i7]],(unsigned long long)1)*max(jc[num[i8]],(unsigned long long)1)*max(jc[num[i9]],(unsigned long long)1));
                if(i7>0) ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9+i0-1]/(max(jc[num[i1]],(unsigned long long)1)*max(jc[num[i2]],(unsigned long long)1)*max(jc[num[i3]],(unsigned long long)1)*max(jc[num[i4]],(unsigned long long)1)*max(jc[num[i5]],(unsigned long long)1)*max(jc[num[i6]],(unsigned long long)1)*max(jc[num[i7]-1],(unsigned long long)1)*max(jc[num[i8]],(unsigned long long)1)*max(jc[num[i9]],(unsigned long long)1));
                if(i8>0) ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9+i0-1]/(max(jc[num[i1]],(unsigned long long)1)*max(jc[num[i2]],(unsigned long long)1)*max(jc[num[i3]],(unsigned long long)1)*max(jc[num[i4]],(unsigned long long)1)*max(jc[num[i5]],(unsigned long long)1)*max(jc[num[i6]],(unsigned long long)1)*max(jc[num[i7]],(unsigned long long)1)*max(jc[num[i8]-1],(unsigned long long)1)*max(jc[num[i9]],(unsigned long long)1));
                if(i9>0) ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9+i0-1]/(max(jc[num[i1]],(unsigned long long)1)*max(jc[num[i2]],(unsigned long long)1)*max(jc[num[i3]],(unsigned long long)1)*max(jc[num[i4]],(unsigned long long)1)*max(jc[num[i5]],(unsigned long long)1)*max(jc[num[i6]],(unsigned long long)1)*max(jc[num[i7]],(unsigned long long)1)*max(jc[num[i8]],(unsigned long long)1)*max(jc[num[i9]-1],(unsigned long long)1));
            }
        }
    }
    void tiao0n()
    {
        ans+=jc[i1+i2+i3+i4+i5+i6+i7+i8+i9]/(jc[num[1]]*jc[num[2]]*jc[num[3]]*jc[num[4]]*jc[num[5]]*jc[num[6]]*jc[num[7]]*jc[num[8]]*jc[num[9]]);
    }
    
    void tiao9y()
    {
        for(int i=1;i<=num[9];i++)
        {
            i9=i;
            if(num[0]>0) tiao0y();
            else tiao0n();
        }
    }
    void tiao9n()
    {
        i9=0;
        if(num[0]>0) tiao0y();
        else tiao0n();
    }
    
    void tiao8y()
    {
        for(int i=1;i<=num[8];i++)
        {
            i8=i;
            if(num[9]>0) tiao9y();
            else tiao9n();
        }
    }
    void tiao8n()
    {
        i8=0;
        if(num[9]>0) tiao9y();
        else tiao9n();
    }
    
    void tiao7y()
    {
        for(int i=1;i<=num[7];i++)
        {
            i7=i;
            if(num[8]>0) tiao8y();
            else tiao8n();
        }
    }
    void tiao7n()
    {
        i7=0;
        if(num[8]>0) tiao8y();
        else tiao8n();
    }
    
    void tiao6y()
    {
        for(int i=1;i<=num[6];i++)
        {
            i6=i;
            if(num[7]>0) tiao7y();
            else tiao7n();
        }
    }
    void tiao6n()
    {
        i6=0;
        if(num[7]>0) tiao7y();
        else tiao7n();
    }
    
    void tiao5y()
    {
        for(int i=1;i<=num[5];i++)
        {
            i5=i;
            if(num[6]>0) tiao6y();
            else tiao6n();
        }
    }
    void tiao5n()
    {
        i5=0;
        if(num[6]>0) tiao6y();
        else tiao6n();
    }
    
    void tiao4y()
    {
        for(int i=1;i<=num[4];i++)
        {
            i4=i;
            if(num[5]>0) tiao5y();
            else tiao5n();
        }
    }
    void tiao4n()
    {
        i4=0;
        if(num[5]>0) tiao5y();
        else tiao5n();
    }
    
    void tiao3y()
    {
        for(int i=1;i<=num[3];i++)
        {
            i3=i;
            if(num[4]>0) tiao4y();
            else tiao4n();
        }
    }
    void tiao3n()
    {
        i3=0;
        if(num[4]>0) tiao4y();
        else tiao4n();
    }
    
    void tiao2y()
    {
        for(int i=1;i<=num[2];i++)
        {
            i2=i;
            if(num[3]>0) tiao3y();
            else tiao3n();
        }
    }
    void tiao2n()
    {
        i2=0;
        if(num[3]>0) tiao3y();
        else tiao3n();
    }
    
    void tiao1y()
    {
        for(int i=1;i<=num[1];i++)
        {
            i1=i;
            if(num[2]>0) tiao2y();
            else tiao2n();
        }
    }
    void tiao1n()
    {
        i1=0;
        if(num[2]>0) tiao2y();
        else tiao2n();
    }
    
    
    int main()
    {
        std::ios::sync_with_stdio(false);
    
        long long shu;
        jc[0]=1;
        for(int i=1;i<=18;i++)
        {
            jc[i]=jc[i-1]*i;
        }
        cin>>shu;
        while(shu)
        {
            num[shu%10]++;
            shu/=10;
            tj++;
        }
        if(num[1]>0) tiao1y();
        else tiao1n();
        cout<<ans<<endl;
        return 0;
    }