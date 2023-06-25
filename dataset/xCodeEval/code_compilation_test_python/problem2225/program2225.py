def program2225():
    //Suffix Structures
    
    import java.util.Scanner;
    
    public class Pro08 {
    
    	public static void main(String[] args) {
    		Scanner sc = new Scanner(System.in);
    		String s, t;
    		int count_s[] = new int[30];
    		int count_t[] = new int[30];
    		
    		s = sc.next();
    		t = sc.next();
    		for (int i=0;i<s.length();i++)
    			count_s[(int)s.charAt(i) - (int)'a']++;
    		for (int i=0;i<t.length();i++)
    			count_t[(int)t.charAt(i) - (int)'a']++;
    		
    		boolean flag = true;
    		for (int i=0;i<26;i++)
    			if (count_s[i] < count_t[i])
    				flag = false;
    		
    		if (!flag)
    			System.out.print("need tree");
    		else {
    			if (s.length() == t.length() && !s.equals(t)){
    				System.out.print("array");
    				return;
    			}
    			int i = 0;
    			int index = 0;
    			while (i < s.length() && index < t.length()) {
    				if (s.charAt(i) == t.charAt(index))
    					index++;
    				i++;
    			}
    			
    			if (index == t.length())
    				System.out.print("automaton");
    			else
    				System.out.print("both");
    		}
    	}
    }