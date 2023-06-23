def program1055():
    #include <iostream>
    #include <stdio.h>
    #include <stdlib.h>
    #include <math.h>
    
    using namespace std;
    
    int main()
    {
        int num;
        scanf("%d", &num);
        int result = pow(2,num+1) - 2;
        printf("%d", result);
    }