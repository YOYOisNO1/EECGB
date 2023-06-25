def program3790():
    #include<iostream>
    #include<string.h>
    #include<algorithm>
    using namespace std;
    
    int main() {
    	long long n, x, y;
    	cin >> n;
    	cin >> x >> y;
    	if(x + y <= n + 1) {
    		cout << "White" << endl;
    	} else {
    		cout << "Black" << endl;
    	}
    	return 0;
    }