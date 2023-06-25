def program3192():
    #define _CRT_SECURE_NO_WARNINGS
    #include<stdio.h>
    #include<stdlib.h>
    int main(void)
    {
    	int x1 = 0;
    	int x2 = 0;
    	int x3 = 0;
    	int x4 = 0;
    	int x5 = 0;
    	int x6= 0;
    	int y1 = 0;
    	int y2 = 0;
    	int y3 = 0;
    	int y4 = 0;
    	int y5 = 0;
    	int y6 = 0;
    	while (scanf("%d %d %d %d %d %d %d %d %d %d %d %d", &x1, &y1, &x2, &y2, &x3, &y3, &x4, &y4, &x5, &y5, &x6, &y6) != EOF)
    	{
    
    		if ((x1 >= x5) && (x1 >= x3) && (x2 <= x4) && (x2 <= x6) && (y4 >= y2) && (y5 <= y1) && (y6 >= y3)|| (x1 >= x3) && (x2 <= x4) && (y3 <= y1) && (y4 >= y2)|| (x1 >= x5) && (y1 >= y5) && (x6 >= x2) && (y6 >= y2))
    		{
    			printf("NO\n");
    		}
    
    
    		else
    			printf("YES\n");
    
    	}
    	system("pause");
    
    }