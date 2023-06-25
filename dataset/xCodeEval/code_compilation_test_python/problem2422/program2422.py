def program2422():
    #include <stdio.h>
    
    void main()
    {
    	int hr, mi;
    	scanf("%d:%d", &hr, &mi);
    	printf("%d %d\n", mi*6, ((hr%12)*30 + mi*0.5));
    }