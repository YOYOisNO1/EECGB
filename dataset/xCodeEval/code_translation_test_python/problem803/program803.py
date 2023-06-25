    
    
def main():
        N = int(input())
        vals = [int(i) for i in input().split()] 
        
        sum = 0
        max = 0
    
        for x in vals:
            sum = sum + x
            if x > max:
                max = x
        new_sum = 0
        curr_test = max;
    
        while new_sum <= sum:
            new_sum = 0
            for x in vals:
                new_sum = new_sum + (curr_test - x)
            curr_test = curr_test + 1
    
        print(curr_test - 1)
    
    main()