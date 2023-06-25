def program2522():
    package javaapplication2;
    
    import java.util.Arrays;
    import java.util.Scanner;
    
    public class test {
          public static void main(String[] args) {
            
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int a[] = new int[n];
            for(int i =0;i<n;i++){
                a[i] = sc.nextInt();
            }
            Arrays.sort(a);
            int sum = 0;
            for(int i = 0;i<(a.length - 1);i = i+2){
                sum += Math.abs(a[i] - a[i+1]);
                
                
            }
              System.out.println(sum);
           
            
            
        }
    }