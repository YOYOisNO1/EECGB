def program1830():
    #include <cstdio>
    using namespace std;
    
    int li[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
    
    int count(int n){
        int ret = 0;
        while (n > 0) {
            ret += li[n%10];
            n /= 10;
        }
    
        return ret;
    }
    
    int main() {
        int a, b;
        scanf("%d%d", &a, &b);
    
        int cnt = 0;
        for (int i = a; i <= b; i++) {
            cnt += count(i);
        }
    
        printf("%d\n", cnt);
    
        return 0;
    }