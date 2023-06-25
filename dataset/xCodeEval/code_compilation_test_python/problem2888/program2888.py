def program2888():
    #include <iostream>
    using namespace std;
    int main(){
    	int n;
    	cin >> n;
    	char arr[50];
    	cin >> arr;
    	int b = 0;
    	for (int i = 0; i < n; i++){
    		if (arr[i] == 'B') b++;
    	}
    	long long c = 0;
    	while (b){
    		for (int i = 0; i < n; i++){
    			if (arr[i] == 'R'){
    				arr[i] = 'B';
    				b++;
    			} else {
    				arr[i] = 'R';
    				b--;
    				break;
    			}
    		}
    		c++;
    	}
    	cout << c << endl;
    }