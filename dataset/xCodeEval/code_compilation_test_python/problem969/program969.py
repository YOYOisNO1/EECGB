def program969():
    #include<cstdio>
    int TUX,FOO=0,BAR=0,BAZ=0,QUZ=1;
    int main(){
    	#ifdef local
    	freopen("data.in","r",stdin),freopen("data.out","w",stdout);
    	#endif
    	scanf("%d",&TUX);
    	for(int i=1;i<=TUX;++i){
    		int PUR;scanf("%d",&PUR);
    		FOO=FOO+PUR;
    		BAR=BAR+1;
    		if(FOO*QUZ>BAZ*BAR) BAZ=FOO,QUZ=BAR;
    	}
    	printf("%.6lf\n",BAZ*1.0/QUZ);
    	return 0;
    }