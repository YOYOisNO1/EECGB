    memoization_table = {}
    
def compute_count(previous_max, rest):
        global memoization_table 
        original_rest = rest
    
        if (previous_max, rest) in memoization_table:
            return memoization_table[(previous_max, rest)] 
    
        num_digits = len(str(rest))
    
        if num_digits == 1:
            memoization_table[(previous_max, original_rest)] = 1, min(0, rest-previous_max) 
            return 1, min(0, rest-previous_max) 
    
        sum_count = 0
        while rest > 0:
            s = str(rest).zfill(num_digits)
            new_max = max(previous_max, int(s[0])) 
            new_rest = int(s[1:])
            count, leftover = compute_count(new_max, new_rest) 
    
            sum_count += count 
            rest -= new_rest
            rest += leftover
    
        memoization_table[(previous_max, original_rest)] = sum_count, rest
        return sum_count, rest
    
    print(compute_count(0, int(input())[0])
    
            
    