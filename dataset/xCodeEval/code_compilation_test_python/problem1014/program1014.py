def program1014():
    #include <iostream>
    using namespace std;
    #include <cmath>
    int main(){
    	int n, k, p;
    	cin >> n;
    	k = log10(n);
    	p = pow(10, k) * floor(n / pow(10, k) + 1) - n;
    	cout << p;
    	return 0;
    }