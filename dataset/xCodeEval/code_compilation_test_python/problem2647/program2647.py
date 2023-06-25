def program2647():
    #include <stdio.h>
    #include <iostream>
    #include <vector>
    #include <string>
    
    #define for0(i,n) for (int i = 0; i < n; i++)
    #define for1(i,n) for (int i = 1; i <= n; i++)
    #define sz(x) ((int)x.size())
    #define all(x) (x).begin(), (x).end()
    #define pb(x) push_back(x)
    #define mp(x, y) make_pair(x, y)
    
    typedef long long int64;
    
    
    using namespace std;
    
    
    
    
    int x0, y0, x1, y1;
    vector <string> turns;
    int num;
    
    
    string move(int dx, int dy) {
    	string res = "";
    	if (dx == -1) res += "L";
    	if (dx == 1) res += "R";
    	if (dy == -1) res += "D";
    	if (dy == 1) res += "U";
    	return res;
    }
    
    bool isgood(int x, int dx, int xx) {
    	if (dx > 0) return x + dx <= xx;
    	if (dx < 0) return x + dx >= xx;
    	return true;
    }
    
    void go(int dx, int dy) {
    	while ( isgood(x0, dx, x1) && isgood(y0, dy, y1) ) {
    		//cout << x0 << " " << y0 << endl;
    		//cout <<  "go " << dx << " " << dy  << endl; 
    		++num;
    		turns.pb( move(dx,dy) );
    		x0 += dx;
    		y0 += dy;
    	}
    }
    
    
    int main () {
    	//freopen("input.txt","rt",stdin);
    	//freopen("output.txt","wt",stdout);
    
    
    	string s1, s2;
    	cin >> s1 >> s2;
    
    	x0 = s1[0] - 'a';
    	y0 = s1[1] - '1';
    	
    	x1 = s2[0] - 'a';
    	y1 = s2[1] - '1';
    
    	cout << x0 << " " << y0 << " " << x1 << " " << y1 << endl;
    	for (int dx = -1; dx <= 1; dx += 2) { 
    		for (int dy = -1; dy <= 1; dy += 2) {
    			while ( isgood(x0,dx,x1) && isgood(y0,dy,y1) ) {
    				//cout << "go " << dx << " " << dy  << endl; 
    				x0 += dx;
    				y0 += dy;
    				turns.pb ( move(dx,dy) );
    				++num;
    			} 
    		}
    	}
    	
    	go(0,1);
    	go(0,-1);
    	go(1,0);
    	go(-1,0);
    
    	cout << num << endl;
    	for (int i = 0; i < sz(turns); ++i) {
    		cout << turns[i] << endl;
    	}
    
    
    
    
    
    	return 0;
    }