    import sys
    from math import *
    
def gcl(x, y):
        fc = sqrt(x**2 + y**2)
        c = int(fc)
        if c % 2 == 0:
            result = 'black'
        else:
            result = 'white'
        if not ((x > 0 and y > 0) or (y < 0 and x < 0)):
            if result == 'black':
                result = 'white'
            else:
                result = 'black'
                
        if c == fc:
            result = 'black'
        return result
    
def main(argv=None):
        if argv is None:
            argv = sys.argv
        print gcl(int(argv[1]), int(argv[2]))
        
    if __name__ == "__main__":
        sys.exit(main())