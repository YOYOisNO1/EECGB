def program661():
    #include <iostream>
    
    using namespace std;
    
    int main(){
        int n;
        cin>>n;
        int matrix[n][n];
        for(int i=0;i<n;++i)
            for(int j=0;j<n;++j)
                cin>>matrix[i][j];
        for(int k=0;k<n;++k){
            for(int i=0;i<n;++i){
                for(int j=0;j<n;++j){
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j]);
                }
            }
        }
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j){
                cout<<matrix[i][j]<<" ";
            }
            cout<<endl;
        }
    }