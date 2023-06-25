    '''
    Created on Apr 20, 2012
    
    @author: Tobias Flach
    '''
    
def solve():
        prime = 1000000007
        
        str_a = input()
        str_b = input()
        k = int(input())
        
        good_shifts = 0
        bad_shifts  = 0
        
        for i in range(0, len(str_a)):
            shifted = str_a[i:] + str_a[:i]
            if shifted == str_b:
                good_shifts += 1
            else:
                bad_shifts += 1
        
        good_sols = 0
        bad_sols  = 0
        if str_a == str_b:
            good_sols = 1
        else:
            bad_sols  = 1
        
        for i in range(0, k):
            t_good_sols = good_sols * (good_shifts - 1) + bad_sols * good_shifts
            t_bad_sols  = good_sols * bad_shifts + bad_sols * (bad_shifts - 1)
            good_sols = t_good_sols % prime
            bad_sols  = t_bad_sols % prime
            
        print "%d" % (good_sols)
    
    if __name__ == '__main__':
        solve()