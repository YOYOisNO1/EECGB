def program3042():
    import math
    
    n = int(input())
    
    a = 1
    b = n
    
    m=int(math.sqrt(n))
    
    for i in range(1, m+1):
    
        x = i
        if n % x == 0:
            y = n // x
            if b - a > y - x:
                a = x
                b = y
    
    print(a, b)
    /*
    #include<bits/stdc++.h>
    using namespace std;
    int main()
    {
        vector<int>arr;
        vector<int>brr;
        int n;
        cin>>n;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(i*j==n)
                {
                    arr.push_back(i);
                    arr.push_back(j);
                }
            }
        }
        /*for(int i=0;i<arr.size();i++){
            cout<<arr[i]<<" ";
        }
        */
        /*cout<<endl;
        for(int j=0;j<brr.size();j++){
            cout<<brr[j];
        }*/
        //cout<<endl;
        int x;
        for(int i=0;i<arr.size();i+=2){
            x = arr[i+1]-arr[i];
            brr.push_back(abs(x));    
            
        }
        
        sort(brr.begin(),brr.end());
        
        for(int j=0;j<arr.size();j++){
            if((arr[j+1]-arr[j])==brr[0])
            {
                cout<<arr[j]<<" "<<arr[j+1];
            }
        }
        */
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    }