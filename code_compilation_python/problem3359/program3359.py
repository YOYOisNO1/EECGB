def program3359():
    #include<stdio.h>
    #include<math.h>
    
    int check(int n){
    	int limit = ceil((double)sqrt(n));
    	int i;
    	for(i=3; i<=limit; i+=2){
    		if(n%i==0){
    			return(i);
    		}
    	}
    	return(n);
    }
    
    int main(){
    	int p,y,i;
    	scanf("%d %d",&p, &y);
    	int ans=-1;
    	if(y%2==0){
    		y--;
    	}
    	
    	for(i=y ; i>p ; i-=2){
    		int q = check(i);
    		if(q>p){
    			ans=i;
    			break;
    		}
    	}
    	printf("%d\n",ans);
    }