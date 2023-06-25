def check(coor1, coor2, coor3):
        v1 = [coor2[i] - coor1[i] for i in range(5)]
        v2 = [coor3[i] - coor1[i] for i in range(5)]
        # print(v1, v2)
        return scalar_product(v1, v2)
    
def scalar_product(coor1, coor2):
        a1, a2, a3, a4, a5 = coor1
        b1, b2, b3, b4, b5 = coor2
        return (a1 * b1 + a2 * b2 + a3 * b3 + a4 * b4 + a5 * b5)
        
        
    n = int(input())
    idx___coor = []
    for idx in range(n):
        coor = [int(x) for x in input().split()]
        idx___coor.append(coor)
    if n > 129:
        print(0)
    else:
        good_idxes = []
        for idx1, coor1 in enumerate(idx___coor):
            is_ok_flag = True
            for idx2, coor2 in enumerate(idx___coor):
                for idx3, coor3 in enumerate(idx___coor):
                    # print(pairs_checked)
                    if idx2 == idx3 or idx1 == idx3 or idx1 == idx2 or not is_ok_flag:
                        continue
                    if check(coor1, coor2, coor3) > 0:
                        is_ok_flag = False
                    # print(pairs_checked, is_ok_flag, idx1, idx2, idx3)
            if is_ok_flag:
                good_idxes.append(idx1)
                    
        good_idxes = sorted(good_idxes)
        good_idxes = [(x + 1) for x in good_idxes]
        print(len(good_idxes))
        print(*good_idxes)