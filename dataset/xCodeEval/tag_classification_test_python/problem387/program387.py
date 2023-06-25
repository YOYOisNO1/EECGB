def solve():
        num, one_pack, two_pack, three_pack = map(int,input().split())
        temp = 4 - (num % 4)
        # print(temp)
        if temp == 1:
            if two_pack >= three_pack * 2:
                if one_pack >= three_pack * 3:
                    return three_pack * 3
            if one_pack >= three_pack + two_pack:
                return three_pack + two_pack
            return one_pack
        elif temp == 2:
            if one_pack >= three_pack:
                if two_pack >= three_pack * 2:
                    return three_pack * 2
            if two_pack >= one_pack * 2:
                return one_pack * 2
            return two_pack
        elif temp == 3:
            if two_pack >= one_pack * 2:
                if three_pack >= one_pack * 3:
                    return one_pack * 3
            if three_pack >= two_pack + one_pack:
                return two_pack + one_pack
            return three_pack        
        else:
            return 0
    
    print(solve())