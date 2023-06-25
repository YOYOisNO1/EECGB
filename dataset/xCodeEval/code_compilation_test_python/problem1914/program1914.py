def program1914():
    /*package whatever //do not write package name here */
    
    import java.io.*;
    import java.util.*;
    
    public class GFG {
    	public static void main (String[] args) {
    		Scanner sc = new Scanner(System.in);
    		int n = sc.nextInt(), k = sc.nextInt();
    		if(k == 1) System.out.println(n);
    		else {
    		    int count = 1, x = 1;
    		    while(x < n) {
    		        x = (int)Math.pow(2, count) + x;
    		        count++;
    		    }
    		    System.out.println(x);
    		}
    	}
    }