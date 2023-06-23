def compose_simple_list(num):
        simple_list = [2]
        for i in range(3, num, 2):
            threashold = simple_list[-1]
            for simple_num in simple_list[1:]:
                if simple_num < threashold:
                    if i % simple_num == 0:
                        break
                    else:
                        threashold = i//simple_num
            else:
                simple_list.append(i)
        return simple_list
    
    
def is_simple(num):
        threshold = num//2
        if num % 2 == 0:
            return False
        for i in range(3, threshold, 2):
            if num % i == 0:
                return False
        else:
            return True
    
    
def get_simple_nums(num):
        if is_simple(num):
            return [num]
        else:
            answer = []
            nearest_simple = -1
            for i in range(num, num//2, -1):
                if is_simple(i):
                    nearest_simple = i
                    break
            if nearest_simple != -1:
                answer.append(nearest_simple)
                left_num = num - nearest_simple
                # now num is even, so it's not simple. but it's quite small.
                simple_list = compose_simple_list(left_num)
                # try to find sum of 2 elements from list as num
                for num1 in simple_list:
                    for num2 in simple_list:
                        if num1 == left_num:
                            answer.append(num1)
                            return answer
                        elif num2 == left_num:
                            answer.append(num2)
                            return answer
                        elif num1 + num2 == left_num:
                            answer.append(num1)
                            answer.append(num2)
                            return answer
                else:
                    raise Exception('no such combination', num, left_num)
    
    
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
        main()
    
        # import timeit
        # for num in range(99999, 90000, -2):
        #     print('time is', timeit.timeit('get_simple_nums(num)', number=1, setup="from __main__ import compose_simple_list, get_simple_nums, num"))
        #     print()
        #
    