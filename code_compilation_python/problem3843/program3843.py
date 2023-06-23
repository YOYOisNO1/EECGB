def program3843():
    #include <iostream>
    #include <string>
    
    using namespace std;
    
    int main(){
    	string inp;
    	cin >> inp;
    	unsigned long long int row;
    	char sira = inp[inp.size()-1];
    	string str = inp.substr(0,inp.size()-1);
    	row = strtoull(str.c_str(), 0, 10);	
    	int array[6] = {4,5,6,3,2,1};
    	unsigned long long qs = ((row - 1) / 8);
    	row = row - (qs*8);
    unsigned long long opo = qs * 32;
    
    if (row == 2 || row == 4)
        opo += 7;
    else if (row == 5 || row == 7)
        opo += 16;
    else if (row == 6 || row == 8)
        opo += 23;
    
    opo += array[sira - 'a'];
    
    cout << opo;return 0;
    }