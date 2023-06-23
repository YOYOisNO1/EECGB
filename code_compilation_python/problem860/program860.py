def find_factor(all):
        i = 2
        list = [0]
        while i < all :
            if all % i == 0 :
                list.append(i)
            i += 1
        return list[1:] #输出所有因数，列表形式输出
    
def if_candiv(str,div_value): #查看该子串是否可分割成值为div_value的串
        left = div_value
        position = 0
        for i in str:
            left -= int(i)
            if left == 0:
                return str[position+1:],"YES"
            elif left < 0:
                return str,"NO"
            position += 1
    
    try:
        while True:
            length = int(input())
            num_str = input().strip("0")
            length = len(num_str)
            all = 0
            for i in num_str:
                all += int(i)
            if all == 0:
                print("YES")
            else :
                factor_list =find_factor(all)
                flag_0 = "NO"
                for factor in factor_list:
                    print(factor)
                    copy_str = num_str
                    position = 0
                    flag_1 = "YES"
                    while position < length :
                        print(copy_str)
                        [copy_str,flag_1] = if_candiv(copy_str,factor)
                        position = length - len(copy_str)
                        if flag_1 == "NO":
                            print(flag_1)
                            break
                    if flag_1 == "YES":
                        flag_0 = "YES"
                        break
                print(flag_0)
    except EOFError:
        pass