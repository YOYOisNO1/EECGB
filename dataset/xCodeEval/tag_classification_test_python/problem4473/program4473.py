    from operator import itemgetter
    from collections import OrderedDict
    
def RocketStages():
        letters = 'abcdefghijklmnopqrstuvwxyz'
        weights = {}
        n,k = map(int,input().split())
        s = input()
    
        for i in s:
            if i not in weights:
                weights[i] = letters.index(i)+1
        
        sorted_weights = OrderedDict(sorted(weights.items(), key=itemgetter(1)))
    
        current = sorted_weights.keys()[0]
        total_weight = sorted_weights[sorted_weights.keys()[0]]
        stages = 1
        for i in sorted_weights:
            if sorted_weights[i]-sorted_weights[current] >= 2 and stages < k:
                total_weight += sorted_weights[i]
                current = i
                stages += 1
    
        if stages == k:
            print(total_weight)
        else:
            print(-1)
    
    RocketStages()