def program2602():
    #include <iostream>
    #include <algorithm>
    
    using namespace std;
    int n, a[105][3], act[105];
    
    int main(){
    	cin >> n;
    	for (int i = 0; i < n; i++)
    		cin >> act[i];
    	a[0][0] = 0; 
    	if (act[0] == 1 || act[0] == 3) a[0][1] = 1; 
    	if (act[0] == 2 || act[0] == 3) a[0][2] = 1;
    	for (int day = 1; day < n; day++) {
    		if (act[day] == 0) {
    			a[day][0] = a[day-1][0];
    			a[day][0] = max(a[day][0], a[day-1][1]);
    			a[day][0] = max(a[day][0], a[day-1][2]);
    		}
    		// cout << a[day][0] << " . ";
    		if (act[day] == 1 || act[day] == 3) 
    			a[day][1] = max(a[day-1][2] + 1, a[day-1][0] + 1);
    		// cout << a[day][1] << " . ";
    		if (act[day] == 2 || act[day] == 3)
    			a[day][2] = max(a[day-1][1] + 1, a[day-1][0] + 1);
    		// cout << a[day][2] << " . ";
    		// cout << endl;
    	}
    	int retVal = a[n-1][0];
    	if (retVal < a[n-1][1]) retVal = a[n-1][1];
    	if (retVal < a[n-1][2]) retVal = a[n-1][2];
    	cout << n - retVal << endl;
    }