    import itertools
    
def split_array(array):
        split_index = list(range(1, len(array)))
        for i in range(len(array)):
            for each_comb in itertools.combinations(split_index, i):
                each_comb = list(each_comb)
                each_comb.insert(0, 0)
                each_comb.insert(len(each_comb), len(array))
    
                index = []
                arrays = []
                for i in range(len(each_comb) - 1):
                    index.append([each_comb[i], each_comb[i + 1]])
                    arrays.append(array[each_comb[i] : each_comb[i + 1]])
                if not 0 in [sum(each_arr) for each_arr in arrays]:
                    return index
        return None
    
    if __name__ == '__main__':
        num = int(input())
        array = [int(x.strip()) for x in input().split(' ')]
    
        index = split_array(array)
        if index:
            print('YES')
            print(len(index))
            for each in index:
                print('%d %d' % (each[0] + 1, each[1]), end='')
                print()
        else:
            print('NO')