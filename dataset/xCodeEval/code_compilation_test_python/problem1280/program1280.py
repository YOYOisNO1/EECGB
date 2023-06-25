def program1280():
    #include <iostream>
    using namespace std;
    bool s[10];
    int main(){
    	int n, m;
    	cin >> n >> m;
    	int a[n], aa;
    	for(int i = 0; i < n; i ++)	cin >> a[i];
    	for(int i = 0; i < m; i ++){
    		cin >> aa;
    		s[aa] = 1;
    	}
    	for(int i = 0; i < n; i ++) if(s[a[i]]) cout << a[i] << " ";
    }