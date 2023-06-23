    
    import math
    
def solve(str):
        if str[1][0] - str[0][0] >= str[0][0]:
            print str[0][1]
            return
        if str[3][0] - str[2][0] >= str[2][0]:
            print str[3][1]
            return
    
        print 'C'
    
    
    
    if __name__ == "__main__":
    
        al = ['A', 'B', 'C', 'D']
        str = []
        for i in xrange(4):
            str.append((len(input()[2:]), al[i]))
    
        str.sort()
        solve(str)
    
    
    
    
    
    