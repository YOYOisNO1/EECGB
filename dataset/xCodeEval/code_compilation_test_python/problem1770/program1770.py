def program1770():
    #include <bits/stdc++.h>
    
    using namespace std;
    
    int main(){
        long long int n;
        int div = 0, tot=0;
    
        cin >> n;
    
        for(int i=2;i<n;i++){
            for(int j=2;j<=10;j++){
                if(i%j==0)
                    div++;
                else
                    continue;
                if(div==9)
                    tot++;
                    break;
            }
        }
        cout << tot << endl;
        
    }
    // 1537624596591