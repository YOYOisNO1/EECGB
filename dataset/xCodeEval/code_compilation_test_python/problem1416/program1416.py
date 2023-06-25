def program1416():
    from sys import stdin
        # stdin = open('input.txt','r')
         
        l1 = stdin.readline().strip().split()
         
        days = int(l1[0])
        sum_time = int(l1[1])
         
        max_times = [None] * days
        min_times = [None] * days
        max_sum = 0
        min_sum = 0
         
        for i in range(days):
            times = stdin.readline().strip().split()
            max_sum += int(times[1])
            min_sum += int(times[0])
            min_times[i] = int(times[0])
            max_times[i] = int(times[1])
         
        if max_sum < sum_time or min_sum > sum_time:
            print("NO")
        else:
            print("YES")
            need = sum_time - min_sum
            for i in  range(days):
                if need == 0:
                    print(min_times[i], end=" ")
                else:
                    if need > (max_times[i] - min_times[i]):
                        print(max_times[i], end=" ")
                        need -= (max_times[i] - min_times[i]) 
                    else:
                        print(min_times[i] + need, end=" ")
                        need = 0