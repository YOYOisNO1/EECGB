    from sys import maxsize, stdout, stdin, stderr;# mod = int(1e9 + 7);#import re  # can use multiple splits
    tup = lambda: map(int, stdin.readline().split())
    I = lambda: int(stdin.readline())
    lint = lambda: [int(x) for x in stdin.readline().split()]
    S = lambda: stdin.readline().replace('\n', '').strip()
#def grid(r, c): return [lint() for i in range(r)]
def debug(*args, c=6): print('\033[3{}m'.format(c), *args, '\033[0m', file=stderr)
    stpr = lambda x  : stdout.write(f'{x}' + '\n')
    star = lambda x : print(' '.join(map(str , x)))
    from itertools import permutations
    
    n = I()
    x = I()
    arr =['012',
          '102',
          '120',
          '210',
          '201',
          '021']
    #REPEATING THE SAME MOVES EVERY TIME 
    print(arr[n%6][x])
    
    
    
    
    
    
    
    
    