def program3075():
    #include<iostream>
    using namespace std;
        int main(){
            int n;
            cin>>n;
            string s="";
            for(i=1;i<=1000;i++){
                s=s+char(i);
            }
            cout<<s[n-1]<<endl;
            return 0;
       }