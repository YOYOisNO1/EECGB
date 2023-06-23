def program3393():
    #include <iostream>
    using namespace std;
    
    int gcd(int a,int b){
        if(b == 0){
            return a; 
        }
        else{
            return gcd(b,a%b); 
        }
    }
    
    int main(){
    	int a; 
    	int b;
    	cin >> a >> b;
    
    	int aa = a / gcd(a, b);
    	int bb = b / gcd(a, b);
    
    	while (true){
    		if(abs(aa-bb)==1){
    			cout << "Eqular" << endl;
    			break;
    		}
    		if(a < b){
    			cout << "Dasha" << endl;
    			break;
    		}
    		if(a > b){
    			cout << "Masha" << endl;
    			break;
    		}
    	}
    
    }