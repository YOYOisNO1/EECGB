def program547():
    #include <iostream>
    using namespace std;
    
    int main() {
    	int a,b,c,x,y,z;
    	cin>>a>>b>>c;
    	cin>>x>>y>>z;
    	int x1= x-a;
    	int x2= y-b;
    	int x3= z-c;
    	int sum = x1+x2+x3;
    	if(sum!=-3){
    	    cout<<"No";
    	}
    	else cout<<"Yes";
    	return 0;
    }