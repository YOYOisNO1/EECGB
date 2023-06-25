def program1894():
    
    from sys import stdin
    
    planet_count, goods_count, volume = tuple( int(p) for p in stdin.readline().split() )
    names = []
    buy_prices = [ [0] * goods_count for i in xrange(planet_count) ]
    sale_prices = [ [0] * goods_count for i in xrange(planet_count) ]
    count = [ [0] * goods_count for i in xrange(planet_count) ]
    
    for i in xrange(planet_count):
        names.append( stdin.readline() )
        for j in xrange(goods_count):
            buy_prices[i][j], sale_prices[i][j], count[i][j] = tuple( int(p) for p in stdin.readline().split() )
    
    max_profit = 0
    goods = range(goods_count)
    get_profit = lambda src, dst, good_index: sale_prices[dst][good_index] - buy_prices[src][good_index]
    for i in xrange(planet_count):
        for j in xrange(planet_count):
            goods.sort(key=lambda index: get_profit(i, j, index), reverse=True)
            available_volume = volume
            this_profit = 0
            for good_index in goods:
                if get_profit(i, j, good_index) <= 0:
                    break
                vol = min(available_volume, count[i][good_index])
                this_profit += get_profit(i, j, good_index) * vol
                available_volume -= vol
            max_profit = max(max_profit, this_profit)
    
    print(max_profit)
    