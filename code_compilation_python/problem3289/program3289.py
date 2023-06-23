def program3289():
    #include <bits/stdc++.h>
    using namespace std;
    
    int main(){
        long long int n, k;
        cin>>n>>k;
        long long int arr[n];
        for(int i=0;i<n;i++) arr[i] = i+1;
        long long int low = 0;
        long long int high = sizeof(arr)/sizeof(arr[0]);;
        //cout<<low<<" "<<high;
        int count = 0;
        //cout<<arr[low]<<" "<<arr[high];
        while(low < high){
            if(arr[low] + arr[high] == k){
                count++;
                low++;
                high--;
            }else if(arr[low] + arr[high] < k)
                low++;
            else
                high--;
        }
        cout<<count<<endl;
        return 0;
    }