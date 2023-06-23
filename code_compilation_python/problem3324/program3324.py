def program3324():
    #include <iostream>
    #include <algorithm>
    #include <set>
    #include <vector>
    #include <sstream>
    #include <typeinfo>
    
    using namespace std;
    
    int main() {
    	int a, b;
    	cin >> a >> b;
    	string s;
    	cin >> s;
    	int c = s.size();
    	int xb[100], yb[100];
    	int x = 0, y = 0;
    	for (int i = 0; i < c; i++) {
    		switch (s[i]) {
    			case 'U':
    				y++;
    				break;
    			case 'D':
    				y--;
    				break;
    			case 'L':
    				x--;
    				break;
    			case 'R':
    				x++;
    				break;
    		}
    		xb[i] = x;
    		yb[i] = y;
    	}
    	int xr = xb[c-1], yr = yb[c-1];
    	for (int i = 0; i < c; i++) {
    		int xu = a - xb[i];
    		int yu = b - yb[i];
    		int resx, resy;
    		if (xr == 0) {
    			resx = xu;
    		} else {
    			resx = xu % xr;			
    		}
    		if (yr == 0 && yu != 0) {
    			resy = yu;
    		} else {
    			resy = yu % yr;
    		}
    		if (resx == 0 && resy == 0) {
    			if (xr * yu == xu * yr) {
    				printf("Yes\n");
    				return 0;
    			}
    		}
    	}
    	printf("No\n");
    	return 0;
    }