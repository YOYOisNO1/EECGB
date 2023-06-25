def get_num (cards,start_index):
        pair =[]
        for i in range(start_index,n):
            if cards[i] + cards[start_index] == (sum(cards)/n) * 2:
                pair.append(start_index)
                pair.append(i)
        return pair
    
    n = int(input())
    cards = input()
    
    print sum(cards/n)* 2
    for i in range(n):
        print " ".join(map(str,get_num(cards,i))
    