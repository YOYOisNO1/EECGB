def program1229():
    #include<iostream>
    using namespace std;
    int main()
    {
        char a[9];
        for(int i=0;i<9;i++)
            cin>>a[i];
        if(a[0]==a[8]&&a[1]==a[7]&&a[2]==a[6]&&a[3]==a[5])
            cout<<"YES";
        else
            cout<<"NO";
        return 0;
    }