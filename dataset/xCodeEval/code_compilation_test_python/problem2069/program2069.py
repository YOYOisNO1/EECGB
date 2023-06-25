def program2069():
    #include <iostream>
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <cmath>
    #include <cstring>
    #include <unordered_set>
    
    using namespace std;
    
    int main()
    {
        long long a;
        int b[10];
    
        cin >> a;
        while(a)
        {
            ++ b[a % 10];
            a /= 10;
        }
    
        for(int i = 0; i <= 9; ++ i)
        {
            if(b[i])
            {
                
            }
        }
    
        return 0;
    }