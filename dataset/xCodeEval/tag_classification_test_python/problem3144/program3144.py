    #from __builtin__ import xrange
    
    
def is_simple(num):
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        threshold = num//2
        while i <= threshold:
            if num % i == 0:
                return False
            else:
                i += 1
                threshold = num//i
        else:
            return True
    
    
def get_simple_nums(num):
        if is_simple(num):
            return [num]
        else:
            answer = []
            nearest_simple = -1
            for i in xrange(num, num//2, -1):
                if is_simple(i):
                    nearest_simple = i
                    break
            if nearest_simple != -1:
                answer.append(nearest_simple)
                left_num = num - nearest_simple
                # now num is even. either 2 or not simple.
                if left_num == 2:
                    answer.append(left_num)
                    return answer
                else:
                    # from the biggest to smallest - check if it's simple
                    nearest_simple_2 = -1
                    for j in xrange(left_num - 2, left_num//2 - 1, -1):
                        if is_simple(j):
                            nearest_simple_2 = j
                            left_num_2 = left_num - nearest_simple_2
                            if is_simple(left_num_2):
                                answer.append(nearest_simple_2)
                                answer.append(left_num_2)
                                return answer
                    if nearest_simple_2 == -1:
                        raise Exception('couldn\'t find combination')
            else:
                raise Exception('couldn\'t find combination, but should have found!')
    
    
def main():
        num = input()
        try:
            filtered_num = int(num)
        except:
            raise Exception("incorrect input")
        if filtered_num % 2 == 0:
            raise Exception("number should be odd")
        answer = get_simple_nums(filtered_num)
        print(len(answer))
        print(' '.join(str(x) for x in answer))
    
    
    if __name__ == '__main__':
    
    
    # import timeit
    # for num in xrange(700000001, 900000001, 2):
    #print('time is', timeit.timeit('get_simple_nums(436273289)', number=1, setup="from __main__ import get_simple_nums"))
        # import os
        # import psutil
        # process = psutil.Process(os.getpid())
        # print(process.memory_info().rss)
        main()
        # print(process.memory_info().rss)
        # import gc
        # gc.collect()
        # print(process.memory_info().rss)