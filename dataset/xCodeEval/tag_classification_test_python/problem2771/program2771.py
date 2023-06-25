# def sleep_time(time_sleep, alarms):
    #     min_time = 99999
    #     for alarm in alarms:
    #         time_diff = (alarm[0]*60+alarm[1])-(time_sleep[0]*60+time_sleep[1])
    #         if time_diff < 0:
    #             time_diff += 24*60
    #         min_time = min(time_diff, min_time)
            
    #     return min_time//60, min_time%60
    
def last_repeat(seq):
        seen = {}
        last_idx = -1
        for idx, i in enumerate(seq):
            if i not in seen:
                seen[i] = idx
                # print(seen)
            else:
                # print(f'{seen[i]} vs {last_idx}')
                if seen[i] > last_idx:
                    last_idx = seen[i]
                    # print(f'last_idx: {last_idx}')
                    seen[i] = idx
                    # print(seen)
                else:
                    seen[i] = idx
        
        # print(seen)
        return last_idx+1
    
def min_num(number):
        next_num = 9
        nums = 0
        loop = 0
        while number > next_num:
            number -= next_num
            nums = nums + next_num*(10**loop)
            next_num -= 1
            loop += 1
        else:
            nums = nums + number*(10**loop)
        
        
        return nums
            
    
    if __name__ == "__main__":
        # import random
        n_test_cases = int(input())
        solutions = []
        # brute = []
        for i in range(n_test_cases):
            num = int(input())
    
            solutions.append(min_num(num))
            # brute.append(last_repeat_2(seq))
            
        # print(solutions)
        for j in range(len(solutions)):
            print(solutions[j])
            # print('brute: {}'.format(brute[j]))
    
    # if __name__ == "__main__":
        
    #     n_test_cases = int(input())
    #     solutions = []
    #     for i in range(n_test_cases):
    #         things, time_h, time_m = input().split(' ')
    #         things = int(things)
    #         time_h = int(time_h)
    #         time_m = int(time_m)
    #         alarms = []
    #         for j in range(things):
    #             h, m = input().split(' ')
    #             alarms.append((int(h), int(m)))
    #         solutions.append(sleep_time((time_h, time_m), alarms))
    #     for j in range(len(solutions)):
    #         print('{} {}'.format(solutions[j][0], solutions[j][1]))