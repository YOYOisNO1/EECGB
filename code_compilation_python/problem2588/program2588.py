def program2588():
    #include<stdio.h>
    
    int main()
    {
        int n;
        scanf("%d",&n);
    
        int a[n],i;
        for(i=0; i<n; i++){
            scanf("%d",&a[i]);
        }
        if(a[0]%2==0||a[n-1]%2==0){
            printf("NO\n");
        }
        else{
            int count1=0,count2=0;
            for(i=0; i<n; i++){
                count1++;
                if( a[i]%2==1&&count1%2==1){
                    count2++;
                    count1=0;
                }
            }
            if (count2%2==1){
                printf("YES\n");
            }
            else{
                printf("NO\n");
            }
        }
    
        return 0;
    }