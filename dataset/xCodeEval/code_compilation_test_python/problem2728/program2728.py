def program2728():
    #include <iostream>
    
    using namespace std;
    
    int main()
    {
        int n;
        int *home=new int(n);
        int *away=new int(n);
        cin>>n;
        for(int i=0;i<n;i++){
            cin>>home[i];
            cin>>away[i];
        }
        int c=0;
         for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if (i==j){}
                else if(home[i]==away[j])
                    c++;
            }
        }
    
        cout << c << endl;
        return 0;
    }