def program919():
    #include<bits/stdc++.h> 
    using namespace std ; 
    int main() { 
    	
    	int n , x ; 
    	cin >> n  >> x; 
    
    	queue<long long> q; 
    	map<long long , int> dist ; 
    	dist[x] = 0 ;  
    	q.push(x) ; 
    	while (!q.empty()) { 
    
    
    		long long k = q.front() ; 
    		q.pop();  
    		string v = to_string(k) ; 
    		if (v.size() == n) { 
    				cout << dist[k] ; 
    				return 0 ; 
    		}
    		for(auto x : v) { 
    
    			if (x == '0') continue ;
    			long long w = k * int(x - '0') ; 
    			if (!dist.count(w)) { 
    				dist[w] = dist[k] + 1 	; 
    				q.push(w) ;  }
    		}
    
    	}
    	cout << -1 ; 
    	return 0 ; 
    
    }