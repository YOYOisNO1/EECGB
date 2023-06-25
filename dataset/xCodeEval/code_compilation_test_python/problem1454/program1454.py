def program1454():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    int main() {
    	int a;
    	scanf("%i", &a);
    
    	int arr[a];
    	for (int i = 0; i < a; i++) {
    		scanf("%i", &arr[i]);
    	}
    
    	int min = arr[0];
    	for (int i = 0; i < a; i++) {
    		if (arr[i] < min) {
    			min = arr[i];
    		}
    	}
    
    
    	printf("%i", 2 + arr[2] ^ min);
    	return 0;
    }