def program4040():
    #include <iostream>
    #include <cmath>
    using namespace std;
    typedef long long ll;
    ll k;
    
    int main() {
        cin >> k;
        ll res = 0;
        int i,j,jj;
        for (i=0,j=k;i<k&&j>=0;i++) {
            for (;j>=0;j--) {
                ll x,y;
                x = 3*i+1;
                y = 2*j+1;
                if (i&1) y++;
                if (x*x+3*y*y>4*k*k) continue;
                x++;
                y--;
                if (x*x+3*y*y>4*k*k) continue;
                break;
            }
            if (j<0) break;
            jj=j;
            jj+=1;
            jj*=2;
            if ((i&1)==0) jj--;
            if (!i) res+=jj;
            else res+=2*jj;        
        }
        cout << res;
    }