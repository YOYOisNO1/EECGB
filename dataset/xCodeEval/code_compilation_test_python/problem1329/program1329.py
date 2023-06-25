def program1329():
    #include <iostream>
    using namespace std;
    
    int main() {
        int n,v;
        cin>>n>>v;
        if(v>n || v==n)
            cout<<n-1<<endl;
        else{
            int tank = v,amount = v,i;
            for (i=2;i<n+1;i++){
                tank = tank -1;
                if (tank==(n-i))
                    break;
                else{
                    amount +=(v-tank)*i;
                    tank = v;
                }
            }
            cout<<amount;
            
        }
        return 0;
    }