def program457():
    import java.util.*;
    import java.io.*;
     
      
         public class Solution{
             public static void main (String aargs[]){
                 
                Scanner sc = new Scanner(System.in);
                int n = sc.nextInt();
                int m = sc.nextInt();
                
              int ans = 0;
              int []ar= new int[n+1];
              for(int i= 1; i <= n; i++){
                  ar[i] = sc.nextInt();
              }
              int t= 0;
              int c = 0;
              
              for(int i = 1; i <= n; i++){
                 int a = ar[i];
                 int s = a/m+(a%m == 0?0:1);
                 if(s >= t){
                     t = s;
                     c = i;
                 }
              }
              System.out.println(c);
             }
         }