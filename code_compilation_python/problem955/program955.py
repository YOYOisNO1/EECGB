def program955():
    #include<bits/stdc++.h>
    
    using namespace std;
    
    int main()
    {
    	ios::sync_with_stdio(false);
    	int t, s, q; cin >> t >> s >> q;
    	double piste = s;
    	int lecture = 0;
    	double x;
    	double pas = 1-1.0/q;
    	int sol = 1;
    	while(piste < t)
    	{
    		x = q*(piste - lecture);
    		if(piste + x*pas < t) sol++, lecture = 0, piste += x*pas;
    		else break; 
    		
    	}
    	cout << sol << endl;
    	return 0;
    }