def program523():
    number = input()
    
    number_list_form = number.split()
    
    n_range = int(number_list_form[0])
    des_pos = int(number_list_form[1])
    
    if des_pos * 2 - 1 <= n_range:
        print(des_pos * 2 - 1)
    elif des_pos * 2 > n_range and n_range % 2 == 0:
        print((des_pos - (n_range // 2)) * 2)
    elif des_pos * 2 > n_range and n_range % 2 != 0:
        print((des_pos - ((n_range // 2) + 1)) * 2)