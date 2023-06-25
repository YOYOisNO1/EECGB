    source = "><+-.,[]"
    
    t = '';
    
def convert(c, s):
        return bin(8 + s.index(c))[2:]
    
    for c in input():
        t += convert(c, source)
    print(int(t,) 2) % 1000003