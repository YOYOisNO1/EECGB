def program3184():
    from itertools import groupby
    from math import ceil
    print(sum(ceil(len(tuple(i[1])) / 5)for i in groupby(input())))