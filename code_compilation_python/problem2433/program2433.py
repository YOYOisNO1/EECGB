def g(l1, l2):
        dic = {}
        for ls in [l1, l2]:
            ls.append(ls[0])
            ls.append(ls[1])
            num = 2 if ls == l1 else 1
            for i in range(len(ls) - num):
                dic[ls[i + num]] = ls[i]
        return dic, dict(((val, key) for key, val in dic.items()))
    
    left, left_ = g([1, 3, 5, 7, 9, 11, 24, 22], [13, 14, 16, 15])
    top, top_ = g([13, 14, 5, 6, 17, 18, 21, 22], [1, 3, 4, 2])
    right, right_ = g([4, 2, 21, 23, 12, 10, 8, 6], [17, 18, 20, 19])
    bottom, bottom_ = g([15, 16, 7, 8, 19, 20, 23, 24], [9, 10, 12, 11])
    back, back_ = g([1, 2, 18, 20, 12, 11, 15, 13], [21, 23, 24, 22])
    center, center_ = g([3, 4, 17, 19, 10, 9, 16, 14], [5, 6, 8, 7])
    print(center)
    input()
    
    all_dics = [left, left_, right, right_, top, top_, bottom, bottom_, back, back_, center, center_]
    
    vals = [int(elem) for elem in input().split(' ')]
def f(vals):
        for dic in all_dics:
            aux = list(vals)
            for val in dic:
                aux[val - 1] = vals[dic[val] - 1]
            # if dic == left:
                # print(aux)
                # print(vals[0 : 4])
            for i in range(6):
                found = True
                if len(set(aux[4 * i : 4 * (i + 1)])) != 1:
                    found = False
                    break
                if found:
                    print("YES")
                    return
        print("NO")
    
    f(vals)