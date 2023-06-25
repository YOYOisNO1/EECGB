def program2424():
    #include <iostream>
    #include <string>
    using namespace std;
    int main()
    {
        char t;
        int h,m;
        cin >> h >> t >> m;
        h %= 12;
    
        double x = 30*h + 0.5*m, y = 6*m;
        
        cout << x << " " << y;
    
    }