def program2719():
    #include <iostream>
    #include <map>
    #include <utility>
    #include <tuple>
    
    
    std::map<std::tuple<char, long long, long long, long long, long long, long long>, long long> lkp_table;
    
    long long DP(char warrior,
    	long long count,
    	long long acc_footmen,
    	long long acc_horsemen,
    	long long remaining_footmen,
    	long long remaining_horsemen)
    {
      auto args = std::make_tuple(warrior, count,
    			      acc_footmen, acc_horsemen,
    			      remaining_footmen, remaining_horsemen);
      if (lkp_table.count(args)) {
        return lkp_table[args];
      }
    
      if ((warrior == 'f') && (count > acc_footmen)) {
          return 0;
        }
      else if ((warrior == 'h') && (count > acc_horsemen)) {
        return 0;
      }
      else if ((remaining_footmen < 0) || (remaining_horsemen < 0)) {
        return 0;
      }
      else if ((remaining_footmen == 0) && (remaining_horsemen == 0)) {
        return 1;
      }
      else {
        long long result;
        if (warrior == 'f') {
          result = DP('f', count+1, acc_footmen, acc_horsemen,
    		  remaining_footmen-1, remaining_horsemen) +
    	DP('h', 1, acc_footmen, acc_horsemen,
    	   remaining_footmen, remaining_horsemen-1) % 100000000;
        }
        else {
          result = DP('h', count+1, acc_footmen, acc_horsemen,
    		  remaining_footmen, remaining_horsemen-1) +
    	DP('f', 1, acc_footmen, acc_horsemen,
    	   remaining_footmen-1, remaining_horsemen) % 100000000;
        }
        lkp_table[args] = result;
        return result;
      }
    }
    
    
    int main(int argc, char *argv[])
    {
      long long n1, n2, k1, k2;
      std::cin >> n1;
      std::cin >> n2;
      std::cin >> k1;
      std::cin >> k2;
    
      long long result = DP('f', 0, k1, k2, n1, n2) % 100000000;
      std::cout << result << std::endl;
      return 0;
    }