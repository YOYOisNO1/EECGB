def program3357():
    #include <iostream>
    #include <map>
    #include <cmath>
    #include <vector>
    
    using namespace std;
    
    int p, y;
    
    bool IsPrime(int x) {
    	for (int i = 2; i*i <= x; ++i) {
    		if (x % i == 0) return false;
    	}
    	return true;
    }
    
    int main() {
    	while (cin >> p >> y) {
    		int i;
    		for (i = y; i > p; --i) {
    			if (IsPrime(i)) {
    				cout << i << endl;
    				break;
    			}
    		}
    		if (i == p) cout << -1 << endl;
    	}
    	return 0;
    }