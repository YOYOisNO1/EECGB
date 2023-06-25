def program2488():
    //be name khoda
    //Pedram Sadeghian
    // :)
    #include <bits/stdc++.h>
    using namespace std;
    
    long long n,m,k,x,y;
    
    int main(){
    	cin >> n >> m >> k >> x >> y;
    	long long r;
    	if(n!=1){
    		if(n!=2){
    			r = (k-(n*m))/((n-1)*m) +1;
    			if((k-(n*m))%((n-1)*m)!=0)
    				r++;
    		}
    		else{
    			r = (k-(n*m))/(2*m) +1;
    			if((k-(n*m))%(2*m)!=0)
    				r++;
    		}
    	}
    	else{
    		r = (k-(n*m))/(n*m) +1;
    		if((k-(n*m))%(n*m)!=0)
    			r++;
    	}
    	cout << r << " ";
    	r = 0;
    	if(n!=1){
    		r = (k-(n*m))/((n-1)*m)/2 +1;
    	}
    	else{
    		r = (k-(n*m))/(n*m) +1;
    	}
    	cout << r << " ";
    	r = 0;
    	if(n==1){
    		r += k/m;
    		if(k%m>=y)
    			r++;
    	}
    	else{
    		if(x==n){
    			if (k>n*m){
    				r++;
    				k -= (n*m);
    			}
    			r += k/((n-1)*m*2);
    			k %= ((n-1)*m*2);
    			if (k/((n-1)*m)==1){
    				k -= ((n-1)*m);
    				if (k>((n-2)*m)){
    					k -= ((n-2)*m);
    					if(k>=y){
    						r++;
    					}
    				}
    			}
    		}
    		else{
    			if (k>=n*m){
    				r++;
    				k -= (n*m);
    			}
    			r += k/((n-1)*m);
    			if((k/((n-1)*m))%2==1)
    				r--;
    			k %= ((n-1)*m*2);
    			//cout << endl << r << " " << k << endl;
    			if (k/((n-1)*m)==1){
    				r++;
    				k -= ((n-1)*m);
    				if (k>((x-1)*m)){
    					k -= ((n-2)*m);
    					if(k>=y){
    						r++;
    					}
    				}
    			}
    			else{
    				if (k>((n-x-1)*m)){
    					k -= ((n-x-1)*m);
    					if(k>=y){
    						r++;
    					}
    				}
    			}
    		}
    	}
    	cout << r;
    	
    }