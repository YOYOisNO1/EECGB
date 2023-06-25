def program1024():
    #include <iostream>
    
    using namespace std;
    
    int main() {
    
      int n, m;
      cin >> n >> m;
    
        while(m < 50 && n >= 2){
          for(n = n; n < m; n++) {
            if(m%2 != 0 && m%3 != 0) {
              printf("YES\n");
            } else {
              printf("NO\n");
            }
            break;
          }
          break;
        }
    
      return 0;
    }
    
    // 1536371486446