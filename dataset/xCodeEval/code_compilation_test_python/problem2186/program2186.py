def program2186():
    import java.util.*;
    import java.io.*;
    public class Main{
        public static void main(String args[]){
            int n,i,ans=-1;
            Scanner in = new Scanner(System.in);
            n=in.nextInt();
            int[] arr = new int[n];
            for(i=0;i<7;i++) arr[i]=in.nextInt();
            while(n>0){
                for(i=0;i<7;i++){
                    n-=arr[i];
                    if(n<=0){
                        ans=i+1;
                        break;
                    }
                }
            }
            System.out.println(ans);
        }
    }