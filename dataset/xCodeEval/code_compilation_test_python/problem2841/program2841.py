def program2841():
    from itertools import groupby
    from operator import itemgetter as ig
    
    input()
    return ''.join(map(ig(0), groupby(input())))