def program1969():
    #include<bits/stdc++.h>//万能头文件
    using namespace std;
    int a[226982]; 
    int v[1000],prime[1000],m; //筛素数
    int gcd(int x,int y){
        return x%y==0? y:gcd(y,x%y);
    }
    void dabiao(){ //对于无法用公式计算出的数进行打表
        a[1]=1;
        a[30]=4;
        a[56]=a[60]=13;
        a[36]=a[40]=14;
        a[24]=a[54]=15;
        a[48]=52;
        a[64]=267;
    }
    void work2(int p,int q){ //处理公式中的 a(pq^2)
        if(p==2&&q%2==1)a[p*q*q]=5;
        if(q%p==1&&p%2==1)a[p*q*q]=(p+9)/2;
        if(p==3&&q==2)a[p*q*q]=5;
        if(p%2==1&&q%2==1&&q%p==p-1)a[p*q*q]=3;
        if(p%q==1&&p>3&&p%(q*q)!=1)a[p*q*q]=4;
        if(p%(q*q)==1)a[p*q*q]=5;
        if((q%p!=1&&q%p!=p-1)&&p%q!=1)a[p*q*q]=2;
    }
    void work3(int p,int q,int r){ //处理公式中的 a(pqr)
        int opt=(q%p==1)*4+(r%p==1)*2+(r%q==1)*1;
        switch(opt){
            case 0:a[p*q*r]=1;break;
            case 1:a[p*q*r]=2;break;
            case 2:a[p*q*r]=2;break;
            case 3:a[p*q*r]=4;break;
            case 4:a[p*q*r]=2;break;
            case 5:a[p*q*r]=3;break;
            case 6:a[p*q*r]=p+2;break;
            case 7:a[p*q*r]=p+4;break;
        }
    }
    void prework(int n){//筛素数+处理
        memset(v,0,sizeof(v));
        m=0;
    
        for(int i=2;i<=n;i++){
            if(v[i]==0){
                v[i]=i;
                prime[++m]=i;
                //因为3^4和3^5已经大于题目中所给的64,故只考虑2^4和2^5
                //我是直接用i^3作为下标，所以数组一定要开大，否则会RE
                a[i]=1; a[i*i]=2; a[i*i*i]=5;
                a[16]=14; a[32]=51;
                for(int j=1;j<m;j++){       
                    //以下几段处理公式中的 a(pq)
                    if(gcd(i,prime[j]-1)==1) a[i*prime[j]]=1;
                    if(gcd(i,prime[j]-1)==i) a[i*prime[j]]=2;
    
                    if(gcd(prime[j],i-1)==1) a[i*prime[j]]=1;
                    if(gcd(prime[j],i-1)==prime[j]) a[i*prime[j]]=2; 
    
                    work2(i,prime[j]);
                    work2(prime[j],i);
                    for(int k=1;k<j;k++){
                        work3(prime[k],prime[j],i);
                     //注意：在公式中，a(pqr)这种情况是p<q<r的，大小要分清
                    }
                }
            }
            for(int j=1;j<=m;j++){
                if(prime[j]>v[i] || prime[j] > n/i) break;
                v[i*prime[j]] = prime[j];
            }
        }
    }
    int main(){
        int n;
        cin>>n;
    
        prework(62);
        dabiao();
    
        cout<<a[n]<<endl;
        return 0;
        }