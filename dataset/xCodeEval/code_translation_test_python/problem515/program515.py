def program515():
    garland = input()
    
    R = garland.index('R')
    B = garland.index('B')
    Y = garland.index('Y')
    G = garland.index('G')
    
    indices = [R,B,Y,G]; ans = ""
    for index in indices:
        ans += (str(len(list(filter(lambda x: ((index-x)%4 == 0 and
                                               garland[x] == '!'),
                                    range(0,len(garland)))))) +
                ' ')
    print(ans)
                              