def program1817():
    #include <stdio.h>
    
    int main() {
        int count = 0;
        int n, find, result;
        int i, j;
        scanf("%d %d", &n, &find);
        for(i = 1; i <= n; i++){
            for(j = 1; j <= n; j++){
                if(i > find || j > find) {
                    break;
                }
                result = i*j;
                if(result == find){
                    count++;
                    break;
                }
                if(result > find){
                    break;
                }
            }
        }
        printf("%d\n", count);
    }
    // 1541254992279