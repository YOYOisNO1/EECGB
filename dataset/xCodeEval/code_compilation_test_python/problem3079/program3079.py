def program3079():
    #include<stdio.h>
    #include<string.h>
    int main()
    {
        char s[5000];
        int n;
        scanf("%d",&n);
        for (int i=1;i<=400;i++)
        sprintf(s,"%s%d",s,i);
        
        
        printf("%c",s[n]);
    }