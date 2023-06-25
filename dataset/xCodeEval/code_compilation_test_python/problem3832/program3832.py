def program3832():
    //Copyright(c)2016 liuchenrui
    #include<cstdio>
    #include<ctime>
    #include<iostream>
    #include<algorithm>
    #include<cstring>
    using namespace std;
    inline void splay(int &v){
    	v=0;char c=0;int p=1;
    	while(c<'0' || c>'9'){if(c=='-')p=-1;c=getchar();}
    	while(c>='0' && c<='9'){v=(v<<3)+(v<<1)+c-'0';c=getchar();}
    	v*=p;
    }
    #define ld long double
    #include<cmath>
    int main(){
    	//freopen("xxx.in","r",stdin);
    	//freopen("xxx.out","w",stdout);
    	ld a,b,c;
    	cin>>a>>b>>c;
    	ld d=b*b-(ld)4*a*c;
    	d=sqrt(d);
    	//printf("%.10f\n%0.10f",,);
    	double l=(double)((-b+d)/(2*a));
    	double r=(double)((-b-d)/(2*a));
    	if(l<r)swap(l,r);
    	printf("%.10f\n%0.10f",l,r);
    }