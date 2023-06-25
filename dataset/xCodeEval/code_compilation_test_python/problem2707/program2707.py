def program2707():
    #include<iostream.h>
    int main()
    {
        int n;
        int max;
        int sum=0;
        cin>>n;
        int arr[n];
        for(i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        max=arr[0];
        for(i=0;i<n;i++)
        {
            if(arr[i]>max)
            {
                max=arr[i];
            }
            sum=sum+arr[i];
        }
        while((n*max)-sum<=sum)
        {
            max=max+1;
        }
    cout<<max;
    return 0;
    }