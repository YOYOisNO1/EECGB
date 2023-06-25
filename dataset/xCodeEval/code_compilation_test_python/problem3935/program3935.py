def program3935():
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.io.PrintWriter;
    import java.io.StreamTokenizer;
    import java.util.Comparator;
    import java.util.TreeSet;
    
    
    public class A {
    	public class MyComparator implements Comparator<Long[]> {
    
    		@Override
    		public int compare(Long[] arg0, Long[] arg1) {
    			if (arg0[0] * arg1[1] == arg0[1] * arg1[0])
    				return 0;
    			if (arg0[0] * arg1[1] > arg0[1] * arg1[0])
    				return 1;
    			else
    				return -1;
    				
    		}
    		
    	}
    	public static void solve() throws Exception {
    		int n = nextInt();
    		TreeSet<Long[]> s = new TreeSet<Long[]>();
    		for (int i = 0; i < n; i++) {
    			int k = nextInt();
    			int b = nextInt();
    			if (k == 0){
    				continue;
    			}
    			if (k * b < 0){
    				b = -1 * Math.abs(b);
    			}
    			else {
    				b = Math.abs(b);
    			}
    			k = Math.abs(k);
    			Long[] a = new Long[2];
    			a[0] = (long)k;
    			a[1] = (long)b;
    			s.add(a);
    		}
    		out.print(s.size());
    	}
    
    	
    	
    	
    	static public PrintWriter out = new PrintWriter(System.out);
    	//static public BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    	
    	static public StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in));
    	public static int nextInt() throws IOException {
    		in.nextToken();
    		return (int)in.nval;
    	}
    	public static String nextString() throws IOException {
    		in.nextToken();
    		return in.sval;
    	}
    
    	public static void main(String[] args) throws Exception {
    		solve();
    		out.flush();
    	}
    	
    	
    }