def program4059():
    # cook your code here
    #8.549e2
    import math
    inp = input()
    inp = inp.split('e')
    
    left = inp[0]
    right = inp[1]
    
    if right == '':
        print(left)
    elif left == '':
        print(0)
    else:
        point_index = left.index('.')
        clean_number = left.replace('.', '')
        length = len(clean_number)
        right = int(right)
        if 1:
            new_complete = clean_number
            new_left = new_complete[0:right+point_index].lstrip('0')
            new_right = new_complete[right+point_index:].rstrip('0')
            if new_left != '' and new_right != '':
                print(new_left) + '.' + new_right
            elif new_right == '' and new_left != '':
                times = right - (length - point_index)
                print(new_left) + ('0' * times)
            elif new_left == '' and new_right != '':
                print('0.') + new_right
            else:
                print(0)
        else:
            print(left) + ('0'*right)
        